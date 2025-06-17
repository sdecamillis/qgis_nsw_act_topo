import os
from collections import defaultdict
import urllib.request
import json
import subprocess
from osgeo import ogr
from qgis import processing
from qgis.utils import iface
from qgis.core import (
    QgsVectorLayer, 
    QgsProject, 
    QgsProcessingUtils, 
    QgsField, 
    QgsFeatureRequest, 
    QgsMessageLog, 
    QgsVectorFileWriter, 
    QgsCoordinateTransformContext,
    QgsMapLayer,
    Qgis,
)
from PyQt5.QtCore import QVariant
import layer_info as li

def addArcGisLayer (url, layer, crs, params):
# PARAMETERS
# url (str): URL of the FeatureServer or MapServer
# layer (str): ArcGIS name of the layer
# crs (QgsCoordinateReferenceSystem): spatial reference for the output layer
# params - a dict which can contain any of:
#   where (str): a WHERE clause for the query filter - default is none
#   extent (dict): spatial filter - in {"xmin":<xmin>,"ymin":<ymin>,"xmax":<xmax>,
#     "ymax":<ymax>} format - default is none
#   filterCrs (str): spatial reference for the spatial filter (in WKT format) - 
#     default is none (if extent is specfied, the extent is assumed to be in the SR 
#     of the ArcGIS source layer)
#   outputFields (str or list) - comma-separated string of output fields - default is "*" (ALL)
#   outputCodeValueFields (str or list) - comma-separated string of output fields for which 
#     code/value mapping translation will be applied - default is none
#   outputFormat (str) - output format - defaults to "json" (not sure if anything else will actually work for PyQGIS)
# NOTE: no checking is carried out on the parameters passed
#
# RETURNS
# outfile - location of the output file (GeoPackage)

# TODO:
#   - check whether outputFields/outputCodeValueFields should be str or list
#   - get Type field name from alias rather than lowercase - DONE?
#   - solve issue with MultiGeometries being inserted into non multi layer (might be tricky)
#   - add ability to pass empty outputFields - currently the function fails if you pass an empty list or string. If you don't pass outputFields at all, you get all (*)
#   - fix Scenario 3 if the Type field is not selected(?) - returns NULL?
#   - investigate MaxRecordCount and see if paging is required
    
    import ssl  # To avoid certificate errors with ACT server

    ssl_context = ssl._create_unverified_context()

    arcGisParams = {
        "where": "1=1",
        "outfields":"*",
        "f":"json"
    }
    
    # Set defaults
    if 'where' in params:
        arcGisParams['where'] = params['where']
    
    if 'extent' in params:
        arcGisParams['geometry'] = params['extent']
    
    if 'filterCrs' in params:
        arcGisParams['inSR'] = {"wkt": params['filterCrs'] }
    
    if 'outputFields' in params:
        arcGisParams['outfields'] = params['outputFields']
    
    if 'outputFormat' in params:
        arcGisParams['f'] = params['outputFormat']
    
    outfile = QgsProcessingUtils.generateTempFilename('output.gpkg')
    
    # Get layers from service
    layersUrl = url + "/layers?f=pjson"
    
    # Download the layers json
    with urllib.request.urlopen(layersUrl, context=ssl_context) as u:
        data = json.loads(u.read().decode())
    
    layersArcGis = data['layers']
    
    availableLayers = dict()
    for l in layersArcGis:
        availableLayers[l['name']] = l['id']
    
    layerUrl = url + '/' + str(availableLayers[layer])
    
    # Build query string component of URL
    queryStr='?'
    for key, value in arcGisParams.items():
        queryStr += key
        queryStr += '='
        if isinstance(value,str):
             queryStr += urllib.parse.quote(value)
        if isinstance(value,list):
             queryStr += urllib.parse.quote(','.join(value))
        if isinstance(value,dict):
             queryStr += urllib.parse.quote(json.dumps(value))
        queryStr += '&'
    
    queryStr = queryStr.rstrip('&')
    
    # Extract data from ArcGIS Server
    # '--config GDAL_HTTP_UNSAFESSL YES' to avoid certificate errors with ACT server
    cmd = 'ogr2ogr --config GDAL_HTTP_UNSAFESSL YES -f GPKG '+outfile+' "'+layerUrl+'/query'+queryStr+'" -t_srs '+crs.authid()
    #print(cmd)
    QgsMessageLog.logMessage("Extracting data for layer: "+ layer+" (URL: "+layerUrl+")", level=Qgis.Info)
    QgsMessageLog.logMessage("Command string: "+cmd, level=Qgis.Info)
    # Suppress Command Window
    #subprocess.run (cmd)
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.run(cmd, startupinfo=si)
    
    # Replace code value fields if required.
    # There seem to be 3 different scenarios in ArcGIS with coded value domains:
    # 1. Basic - applies to all types
    # 2. Type/SubType IDs - not actually coded values, but types/subtypes operate much the same way
    # 3. Types with field-specific coded values - this is where there is a type/subtype field, and the coded
    #    values differ for each type/subtype. Unclear what the difference between types/subtypes is...
    
    # Should generally review the use of QgsVectorLayer vs QgsVectorDataProvider
    if 'outputCodeValueFields' in params:
        layerJsonUrl = url + "/" + str(availableLayers[layer]) + "?f=pjson"
        with urllib.request.urlopen(layerJsonUrl, context=ssl_context) as u:
            dataLayer = json.loads(u.read().decode())
        
        vl = QgsVectorLayer(outfile, 'temp', 'ogr')
        pr = vl.dataProvider()
        featureMapping = defaultdict(dict) # from collections
        renameFields = [] # could also be a list of dicts? Might need to store both old/new names+indexes
        
        # Fields not dependent on a Type Field
        fields = dataLayer['fields']
        aliasToName = defaultdict(dict)
        for f in fields:
            if f['name'] in params['outputCodeValueFields']:
                if f['domain'] is not None and f['domain']['type'] == 'codedValue': # domain always exists, but can be NULL
                    mapping = {}
                    for cv in f['domain']['codedValues']:
                        mapping[cv['code']] = cv['name']
                    tempFieldName = f['name'] + '_-%'
                    pr.addAttributes([QgsField(tempFieldName, QVariant.String)])
                    tempFieldIndex = pr.fieldNameIndex(tempFieldName)
                    renameFields.append(f['name'])
                    for ft in vl.getFeatures():
                        featureMapping[ft.id()][tempFieldIndex] = mapping[ft[f['name']]]
            aliasToName[f['alias']] = f['name']
        
        # Fields dependent on a Type Field
        if 'types' in dataLayer:
            typeFieldCreated = False
            typeFieldName = aliasToName[dataLayer['typeIdField']] #dataLayer['typeIdField'].lower() 
            if typeFieldName in params['outputCodeValueFields']:
                # Create new type field
                vl = QgsVectorLayer(outfile, 'temp', 'ogr') 
                pr = vl.dataProvider()
                tempTypeFieldName = typeFieldName + '_-%'
                pr.addAttributes([QgsField(tempTypeFieldName, QVariant.String)])
                tempTypeFieldIndex = pr.fieldNameIndex(tempTypeFieldName)
                renameFields.append(typeFieldName)
                typeMapping = {}
                typeFieldCreated = True
            for f in dataLayer['types']:
                if 'domains' in f:
                    for fieldName in f['domains']:
                        if f['domains'][fieldName]['type'] == 'codedValue' and fieldName in params['outputCodeValueFields']:
                            mapping = {}
                            for cv in f['domains'][fieldName]['codedValues']:
                                mapping[cv['code']] = cv['name']
                            tempFieldName = fieldName + '_-%'
                            if tempFieldName not in pr.fieldNameMap():
                                pr.addAttributes([QgsField(tempFieldName, QVariant.String)])
                                renameFields.append(fieldName)
                            tempFieldIndex = pr.fieldNameIndex(tempFieldName)
                            for ft in vl.getFeatures(QgsFeatureRequest().setFilterExpression('"'+typeFieldName+'"='+str(f['id']))):
                                featureMapping[ft.id()][tempFieldIndex] = mapping[ft[fieldName]]
                if typeFieldCreated:
                    typeMapping[f['id']] = f['name']
            if typeFieldCreated:
                for ft in vl.getFeatures():
                    featureMapping[ft.id()][tempTypeFieldIndex] = typeMapping[ft[typeFieldName]]
        
        pr.changeAttributeValues(featureMapping)
        fieldMap = pr.fieldNameMap()
        
        # Remove original fields (with code values)
        pr.deleteAttributes([value for (key,value) in fieldMap.items() if key in set(renameFields)])
        fieldMap = pr.fieldNameMap() # fieldMap has changed due to deletion
        pr.renameAttributes({v:k.replace("_-%","") for (k,v) in fieldMap.items() if k.endswith("_-%")})#=> needs to be a dict
        vl.updateFields() # may need to call this earlier, multiple times?? Or not at all?
    
    return outfile

def importQgisNwsTopoLayers(layer_list, style_dir=None):
    layers = QgsProject.instance().mapLayersByName('extent')
    if layers: 
        layer = layers[0]
    else:
        raise Exception('Error: Extent layer not found')
    extent = layer.extent()

    arcGisExtent = {
        "xmin":extent.xMinimum(),
        "ymin":extent.yMinimum(),
        "xmax":extent.xMaximum(),
        "ymax":extent.yMaximum()
    }
    for l in layer_list:
        layer_info = li.layer_info[l]
        print(f"  - {layer_info["layerName"]}...")

        # Settings parameters
        arcGisParams = {
            "filterCrs": layer.crs().toWkt(),
            "extent": arcGisExtent,
        }
        if 'where' in layer_info:
            arcGisParams['where'] = layer_info['where']
        
        if 'outputFields' in layer_info:
            arcGisParams['outputFields'] = layer_info['outputFields']
        
        if 'outputCodeValueFields' in layer_info:
            arcGisParams['outputCodeValueFields'] = layer_info['outputCodeValueFields']

        result = addArcGisLayer(layer_info['url'], layer_info['layer'], layer.crs(), arcGisParams)
        # Consider whether to bother adding layers with 0 features
        layer = QgsVectorLayer(result, layer_info['layerName'], 'ogr')
        QgsProject.instance().addMapLayer(layer)
        # Loading the style at this point may fail on QGIS. Loading styles when all
        # layers are downloaded.
        if style_dir:
            style_path = os.path.join(style_dir, layer_info['layerName']+'.qml')
            if os.path.exists(style_path):
                layer.loadNamedStyle(style_path)
            else:
                print(f'WARNING: no style found for {layer.name()}.')
    return

def saveLayersProjectToGpkg (pathToGpkg, removeEmptyLayers = False, saveProjectToGpkg = False, projectName = 'myProject'):
# PARAMETERS
# path (str): full path to the GeoPackage to save to. If it does not exist it will be created
# removeEmptyLayers (boolean): if True, will remove layers with 0 features when it saves. This can remove clutter. Default is False
# saveProjectToGpkg (boolean): if True, will save the project to the same GeoPackage as the layers. The advantage of this is that the project (including all layers) can be distributed as one file, instead of two. The disadvantage is that projects within GeoPackages can't be seen on the filesystem, so can easily be lost. The alternative is to manually save the project (in a separate file). Default is False
# projectName (str): project name, if the project is saved. Default is 'myProject'
# NOTE: no checking is carried out on the parameters passed
#   Also, if you have layers with duplicate names, you will lose the data from one of them
#   Similar functionality(?) can be obtained from the Package layers tool from the Toolbox
    print('Saving vector layers...')

    if not os.path.exists(pathToGpkg):
        ds = ogr.GetDriverByName('GPKG').CreateDataSource(pathToGpkg)
    
    for id, layer in QgsProject.instance().mapLayers().items():
        if layer.type() != QgsMapLayer.VectorLayer:
            continue
        elif removeEmptyLayers and layer.featureCount() == 0:
            QgsProject.instance().removeMapLayers([id])
            continue
        else:
            options = QgsVectorFileWriter.SaveVectorOptions()
            options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer
            options.layerName = layer.name() 
            _writer = QgsVectorFileWriter.writeAsVectorFormatV3(layer, pathToGpkg, QgsCoordinateTransformContext(), options)
            # change the data source
            # TODO: GET THE TEMPORARY DATA SOURCE AND DELETE IT FROM THE TEMP FOLDER
            layer.setDataSource(pathToGpkg + f'|layername={layer.name()}', layer.name(), 'ogr')
    
    if saveProjectToGpkg:
        uri = 'geopackage:'+pathToGpkg+'?projectName='+projectName # need to encode pathToGpkg? projectName?
        QgsProject.instance().write(uri)
    
    print('--> all vector layers saved.')
    return

def import_local_raster_layer(file_path, layer_name):
    iface.addRasterLayer(file_path, layer_name)
    return

def import_local_vector_layer(file_path, layer_name, style_dir=None):
    vlayer = QgsVectorLayer(file_path, layer_name, "ogr")
    QgsProject.instance().addMapLayer(vlayer)
    if style_dir:
        # Import style for this layer
        style_path = os.path.join(style_dir, layer_name+'.qml')
        if os.path.exists(style_path):
            vlayer.loadNamedStyle(style_path)
        else:
            print(f'WARNING: no style found for {vlayer.name()}.')
    return

def import_extent_layer(settings, style_dir=None):
    print(f"  - extent...")
    extent_layer_path = os.path.join(settings['workDir'], settings['extentLayerFilename'])
    import_local_vector_layer(extent_layer_path, 'extent', style_dir=style_dir)
    return

def import_vegetation_layer(settings, style_dir=None):
    print(f"  - vegetation...")
    # Find relevant tiles to import
    lay_extent = QgsProject.instance().mapLayersByName('extent')[0]
    # Import tiles boundaries
    shapefile = os.path.join(settings['vegetationLayerDir'], 'spot_nswgrs.zip')
    if os.path.exists(shapefile):
        import_local_vector_layer(f"/vsizip/{shapefile}/spot_nswgrs.shp", 'spot_nswgrs')
        lay_veg = QgsProject.instance().mapLayersByName('spot_nswgrs')[0]
        # Identify the tiles intersecting the extent layer
        processing.run("native:selectbylocation", {'INPUT':lay_veg,'PREDICATE':[0],'INTERSECT':lay_extent,'METHOD':0})
        selected_tiles = lay_veg.selectedFeatures()
        # Build the list of intersecting tiles
        tile_list = []
        for tile in selected_tiles:
            tile_list.append(f's5hgps_r{tile['row']}c{tile['column']}_y20082012_bcvm5_r5m.img')
        # Delete tile boundary layer
        QgsProject.instance().removeMapLayer(lay_veg)
        # Import vegetation tiles
        if tile_list:
            for idx, tile in enumerate(tile_list):
                tile_path = os.path.join(settings['vegetationLayerDir'], tile)
                if os.path.exists(tile_path):
                    import_local_raster_layer(tile_path, f'rasterVegetation')
                    # Import style for this layer
                    if style_dir:
                        layers = QgsProject.instance().mapLayersByName(f'rasterVegetation')
                        if layers:
                            layers[idx].loadNamedStyle(os.path.join(style_dir, 'rasterVegetation.qml'))
                else:
                    print(f'--> WARNING: the tile {tile} was not found.')
        else:
            print('--> No intersection of vegetation layers with extent layer found.')
    else:
        print(f'--> The shapefile {shapefile} of the layout of the vegetation layers was not found.')
    return

def import_road_osm_layer(settings, style_dir=None):
    print(f"  - road_osm...")
    extent_layer_path = os.path.join(settings['workDir'], settings['extentLayerFilename'])
    output = processing.run("model:download_road_osm_from_extent_layer", {'extent':extent_layer_path,'road_osm':'TEMPORARY_OUTPUT'})
    import_local_vector_layer(output['road_osm'], 'road_osm', style_dir=style_dir)
    return

def change_layer_position(layer, node):
    root = QgsProject.instance().layerTreeRoot()
    myalayer = root.findLayer(layer.id())
    myClone = myalayer.clone()
    parent = myalayer.parent()
    parent.insertChildNode(node, myClone)
    parent.removeChildNode(myalayer)

def relocate_above_another_layer(layer_name, ref_layer_name):
    root = QgsProject.instance().layerTreeRoot()
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    layer_name_list = [x.name() for x in root.layerOrder()]
    idx = layer_name_list.index(ref_layer_name)
    change_layer_position(layer, idx)

def load_styles(folder_path):
    #Iterate through all layers and save styles
    for layer in QgsProject.instance().mapLayers().values():
        style_path = os.path.join(folder_path, f"{layer.name()}.qml")
        if os.path.exists(style_path):
            layer.loadNamedStyle(style_path)
        else:
            print(f'WARNING: no style found for {layer.name()}.')
    print('--> Loading of styles completed')
    return

def save_vector_layers(settings):
    package_path = os.path.join(settings['workDir'], 'layers.gpkg')
    saveLayersProjectToGpkg(package_path)
    return

def save_styles(folder_path):
    #Ensure the folder exists
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    #Iterate through all layers and save styles
    for layer in QgsProject.instance().mapLayers().values():
        style_path = os.path.join(folder_path, f"{layer.name()}.qml")
        layer.saveNamedStyle(style_path)
        print(f"Saved style for {layer.name()}")
    
    return

# Function to import layer without selected attributes
# def importQgisLayer(layerParam):
#     # To avoid certificate errors with ACT server
#     import ssl

#     layers = QgsProject.instance().mapLayersByName('extent')
#     if layers: 
#         layer = layers[0]
#     else:
#         raise Exception('Error: Extent layer not found')
#     extent = layer.extent()
#     crs = layer.crs()
#     ssl_context = ssl._create_unverified_context()

#     arcGisExtent = {
#         "xmin":extent.xMinimum(),
#         "ymin":extent.yMinimum(),
#         "xmax":extent.xMaximum(),
#         "ymax":extent.yMaximum()
#     }

#     print(f"  - {layerParam["layerName"]}...")

#     # Settings parameters
#     arcGisParams = {
#         "filterCrs": layer.crs().toWkt(),
#         "inSR" : {"wkt": layer.crs().toWkt()},
#         "geometry": arcGisExtent,
#         "where": "1=1",
#         "outfields":"*",
#         "f":"json",
#     }

#     # Set defaults
#     if 'where' in layerParam:
#         arcGisParams['where'] = layerParam['where']
    
#     if 'outputFields' in layerParam:
#         arcGisParams['outfields'] = layerParam['outputFields']
    
#     if 'outputFormat' in layerParam:
#         arcGisParams['f'] = layerParam['outputFormat']
    
#     outfile = QgsProcessingUtils.generateTempFilename('output.gpkg')

#     url = layerParam['url']
#     layer = layerParam['layer']

#     # Get layers from service
#     layersUrl = url + "/layers?f=pjson"
    
#     # Download the layers json
#     with urllib.request.urlopen(layersUrl, context=ssl_context) as u:
#         data = json.loads(u.read().decode())
    
#     layersArcGis = data['layers']
    
#     availableLayers = dict()
#     for l in layersArcGis:
#         availableLayers[l['name']] = l['id']
    
#     layerUrl = url + '/' + str(availableLayers[layer])
    
#     # Build query string component of URL
#     queryStr='?'
#     for key, value in arcGisParams.items():
#         queryStr += key
#         queryStr += '='
#         if isinstance(value,str):
#              queryStr += urllib.parse.quote(value)
#         if isinstance(value,list):
#              queryStr += urllib.parse.quote(','.join(value))
#         if isinstance(value,dict):
#              queryStr += urllib.parse.quote(json.dumps(value))
#         queryStr += '&'
    
#     queryStr = queryStr.rstrip('&')
    
#     # Extract data from ArcGIS Server
#     cmd = 'ogr2ogr --config GDAL_HTTP_UNSAFESSL YES -f GPKG '+outfile+' "'+layerUrl+'/query'+queryStr+'" -t_srs '+crs.authid()
#     #print(cmd)
#     QgsMessageLog.logMessage("Extracting data for layer: "+ layer+" (URL: "+layerUrl+")", level=Qgis.Info)
#     QgsMessageLog.logMessage("Command string: "+cmd, level=Qgis.Info)
#     # Suppress Command Window
#     #subprocess.run (cmd)
#     si = subprocess.STARTUPINFO()
#     si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
#     proc_return = subprocess.run(cmd, startupinfo=si)
    
#     print(proc_return)

#     vlayer = QgsVectorLayer(outfile, layerParam["layerName"], "ogr")
#     QgsProject.instance().addMapLayer(vlayer)

#     return proc_return