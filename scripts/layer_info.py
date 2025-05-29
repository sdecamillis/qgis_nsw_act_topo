# input info of the layers
layer_info = {}

layer_info["plantation"] = {
    "layerName": "plantation",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "GeneralCulturalArea",
    "where": "(classsubtype = 6 AND generalculturaltype IN (0,1,2,3,4))",
    "outputFields":["classsubtype","generalculturaltype"],
    "outputCodeValueFields": ["classsubtype","generalculturaltype"],
}
layer_info["urbanArea"] = {
    "layerName": "urbanArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "GeneralCulturalArea",
    "where": "classsubtype = 7",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["contourBase"] = {
    "layerName": "contourBase",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Elevation_and_Depth_Theme/MapServer",
    "layer": "Contour",
    "outputFields":["classsubtype","elevation","relevance","verticalaccuracy","sourceprogram"],
    "outputCodeValueFields": ["classsubtype","sourceprogram"],
}
layer_info["cadastre"] = {
    "layerName": "cadastre",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Land_Parcel_Property_Theme/MapServer",
    "layer": "Lot",
    "where": "classsubtype = 1",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["cadastreACT"] = {
    "layerName": "cadastreACT",
    "url": "https://services1.arcgis.com/E5n4f1VY84i0xSjy/arcgis/rest/services/ACTGOV_BLOCKS/FeatureServer",
    "layer": "ACTGOV BLOCK",
    #"where": "(LAND_USE_POLICY_ZONES IN ('RZ1: SUBURBAN','RZ2: SUBURBAN CORE','RZ4: MEDIUM DENSITY RESIDENTIAL','RZ5: HIGH DENSITY RESIDENTIAL','IZ1: GENERAL INDUSTRY','IZ2: INDUSTRIAL MIXED USE'))",
    "outputFields":["LAND_USE_POLICY_ZONES", "CURRENT_LIFECYCLE_STAGE"],
    "outputCodeValueFields": ["LAND_USE_POLICY_ZONES"],
}
layer_info["hydroArea"] = {
    "layerName": "hydroArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Water_Theme/MapServer",
    "layer": "HydroArea",
    "outputFields":["hydroname","classsubtype","perenniality"],
    "outputCodeValueFields": ["classsubtype","perenniality"],
}
layer_info["fuzzyExtentWaterArea"] = {
    "layerName": "fuzzyExtentWaterArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Water_Theme/MapServer",
    "layer": "FuzzyExtentWaterArea",
    "outputFields":["hydroname","classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["landformArea"] = {
    "layerName": "landformArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Physiography_Category/MapServer",
    "layer": "DLSArea",
    "outputFields":["generalname","classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["culturalArea"] = {
    "layerName": "culturalArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "GeneralCulturalArea",
    "where": "classsubtype IN (9,10)", # 9:Pondage, 10:DamBatter
    "outputFields":["generalname","classsubtype","generalculturaltype"],
    "outputCodeValueFields": ["classsubtype","generalculturaltype"],
}
layer_info["landformLine"] = {
    "layerName": "landformLine",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Physiography_Category/MapServer",
    "layer": "DLSLine",
    "outputFields":["generalname","classsubtype"], 
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["landformPoint"] = {
    "layerName": "landformPoint",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Physiography_Category/MapServer",
    "layer": "DLSPoint",
    "outputFields":["generalname","classsubtype"], 
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["hydroLine"] = {
    "layerName": "hydroLine",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Water_Theme/MapServer",
    "layer": "HydroLine",
    "where": "hydrotype NOT IN (5, 6)",
    "outputFields":["hydroname","hydronametype","perenniality","relevance"],
}
layer_info["hydroPoint"] = {
    "layerName": "hydroPoint",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Water_Theme/MapServer",
    "layer": "HydroPoint",
    "outputFields":["hydrotype"],
    "outputCodeValueFields": ["hydrotype"],
}
layer_info["waterfall"] = {
    "layerName": "waterfall",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Water_Theme/MapServer",
    "layer": "AncillaryHydroPoint",
    "where": "ancillaryhydrotype = 6",
    "outputFields":["generalname","symbolrotation"],
}
layer_info["npwsReserve"] = {
    # This layer doesn't contain info for ACT, replaced with 'Reserves' layer
    "layerName": "npwsReserve",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Administrative_Boundaries_Theme/Mapserver/",
    "layer": "NPWSReserve",
    "outputFields":["reservename","reservetype","classsubtype"],
    "outputCodeValueFields": ["reservetype"], 
}
layer_info["Reserves"] = {
    "layerName": "Reserves",
    "url": "https://gis.environment.gov.au/gispubmap/rest/services/ogc_services/CAPAD/FeatureServer/",
    "layer": "Protected Areas (CAPAD)",
    "outputFields":["NAME", "TYPE", "TYPE_ABBR"],
    "outputCodeValueFields": ["NAME"],
}
layer_info["stateForest"] = {
    "layerName": "stateForest",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Administrative_Boundaries_Theme/Mapserver/",
    "layer": "StateForest",
    "outputFields":["stateforestname"],
}
layer_info["roadTunnel"] = {
    "layerName": "roadTunnel",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "RoadSegment",
    "where": "operationalstatus NOT IN (3,8) AND roadontype = 3 AND classsubtype <> 8",
    "outputFields":["functionhierarchy","classsubtype","surface","lanecount"],
    "outputCodeValueFields": ["functionhierarchy","classsubtype","surface","lanecount"],
}
layer_info["railwayTunnel"] = {
    "layerName": "railwayTunnel",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "Railway",
    "where": "operationalstatus NOT IN (3,8) AND classsubtype IN (1,2,4) AND railontype = 3",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["wharf"] = {
    "layerName": "wharf",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "TransportFacilityLine",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["runway"] = {
    "layerName": "runway",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "Runway",
    "outputFields":["runwaydefinition"],
    "outputCodeValueFields": ["runwaydefinition"],
}
layer_info["ferryRoute"] = {
    "layerName": "ferryRoute",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "FerryRoute",
    "where": "operationalstatus NOT IN (3,8)",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["floodway"] = {
    # Is there value in this vs standard road?
    "layerName": "floodway",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "RoadSegment",
    "where": "operationalstatus NOT IN (3,8) AND roadontype = 4 AND classsubtype <> 8 AND functionhierarchy IN (1,2,3,4,5,6)",
    "outputFields":["functionhierarchy","classsubtype","surface","lanecount","roadontype"],
    "outputCodeValueFields": ["functionhierarchy","classsubtype","surface","lanecount","roadontype"],
}
layer_info["road"] = {
    "layerName": "road",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "RoadSegment",
    "where": "operationalstatus NOT IN (3,8) AND roadontype NOT IN (2,3) AND classsubtype <> 8", # roadontype = 2,3 - Bridge/Tunnel
    "outputFields":["functionhierarchy","classsubtype","surface","lanecount","roadontype"],
    "outputCodeValueFields": ["functionhierarchy","classsubtype","surface","lanecount","roadontype"],
}
layer_info["railway"] = {
    "layerName": "railway",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "Railway",
    "where": "operationalstatus NOT IN (3,8) AND classsubtype IN (1,2,4) AND railontype IN (1,2)",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["roadBridge"] = {
    "layerName": "roadBridge",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "RoadSegment",
    "where": "operationalstatus NOT IN (3,8) AND roadontype = 2 AND classsubtype <> 8",
    "outputFields":["functionhierarchy","classsubtype","surface","lanecount"],
    "outputCodeValueFields": ["functionhierarchy","classsubtype","surface","lanecount"],
}
layer_info["railwayBridge"] = {
    "layerName": "railwayBridge",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "Railway",
    "where": "operationalstatus NOT IN (3,8) AND classsubtype IN (1,2,4) AND railontype = 2",
    "outputFields":["classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["trafficControlDevice"] = {
    "layerName": "trafficControlDevice",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "TrafficControlDevice",
    "where": "classsubtype IN (1,2)",
    "outputFields":["classsubtype","symbolrotation"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["railwayStation"] = {
    "layerName": "railwayStation",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "TransportFacilityPoint",
    "where": "classsubtype = 6",
    "outputFields":["classsubtype","generalname"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["tankPoint"] = {
    "layerName": "tankPoint",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "TankPoint",
    "outputFields":["tanktype"],
    "outputCodeValueFields":["tanktype"],
}
layer_info["tankArea"] = {
    "layerName": "tankArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "TankArea",
    "outputFields":["tanktype"],
    "outputCodeValueFields":["tanktype"],
}
layer_info["cliffPoint"] = {
    "layerName": "cliffPoint", # Move to geographicPoint?
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poitype = 'Cliff'",
    "outputFields":["poiname"],
}
layer_info["spotHeight"] = {
    "layerName": "spotHeight",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Elevation_and_Depth_Theme/MapServer",
    "layer": "SpotHeight",
    "outputFields":["elevation","relevance"],
}
layer_info["relativeHeight"] = {
    "layerName": "relativeHeight",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Elevation_and_Depth_Theme/MapServer",
    "layer": "RelativeHeight",
    "outputFields":["relativeheight","relevance"],
}
layer_info["culturalLine"] = {
    "layerName": "culturalLine",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "GeneralCulturalLine",
    "outputFields":["generalname","classsubtype"], # limited value in generalculturaltype
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["cableway"] = {
    "layerName": "cableway",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer",
    "layer": "Cableway",
    "where": "operationalstatus IN (1,4,6)",
    "outputFields":["classsubtype"], 
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["transmissionLine"] = {
    "layerName": "transmissionLine",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "ElectricityTransmissionLine",
    "outputFields":["classsubtype"], 
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["culturalPoint"] = {
    # Building Small, Rural Yard, Open Cut Quarry, Underground Mine, Windmill, Tower, Beacon, Hut
    # Building(type:5, culturaltype:0 = small building, :1 = Dwelling), Tower(type:7), Beacon(type:12)
    # Rural Yard(type:4, culturaltype:9), Open Cut Quarry, Underground Mine, Windmill, Hut [GeneralIndustryPoint(type:4)]
    "layerName": "culturalPoint",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "GeneralCulturalPoint",
    "where": "classsubtype IN (5,7,12) OR (classsubtype=4 AND generalculturaltype IN (8,9,11,12)) OR (classsubtype=1 AND generalculturaltype=3 AND generalname LIKE '% HUT')",
    "outputFields":["generalname","classsubtype","generalculturaltype"],
    "outputCodeValueFields": ["classsubtype","generalculturaltype"],
}
layer_info["buildingArea"] = {
    "layerName": "buildingArea",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "GeneralCulturalArea",
    "where": "classsubtype=5",
    "outputFields":["generalname","classsubtype"],
    "outputCodeValueFields": ["classsubtype"],
}
layer_info["buildingComplexPoint"] = {
    # Homestead, Hut (removed because included in poiCommunity)
    #subtype:4 complextype=7 seems more the name of a point of interest
    "layerName": "buildingComplexPoint",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer",
    "layer": "BuildingComplexPoint",
    "where": "(classsubtype=4 AND buildingcomplextype=7 AND generalname IS NOT NULL) OR (classsubtype=2 AND buildingcomplextype=0 AND generalname LIKE '% HUT')",
    "outputFields":["generalname","classsubtype","buildingcomplextype"],
    "outputCodeValueFields": ["classsubtype","buildingcomplextype"],
}
layer_info["stateBorder"] = { 
    # Not using portal.spatial
    "layerName": "stateBorder",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/LPIMap/MapServer",
    "layer": "State_Border",
    "outputFields":["RID"],
}
layer_info["restrictedArea"] = {
    # Not using portal.spatial
    "layerName": "restrictedArea",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/LPIMap/MapServer",
    "layer": "Building_Large",
    "where": "classsubtype=3",
    "outputFields":["classsubtype","generalculturaltype","generalname"],
    "outputCodeValueFields":["classsubtype","generalculturaltype"],
}
layer_info["geographicPoint"] = {
    # Using same sarver section, but diviving info in different groups. See poiLandForm
    "layerName": "geographicPoint",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poitype IN ('Gap / Pass / Saddle','Headland','Mountain Like','Peninsula / Spit','Plateau / Tableland','Island','Rapids','Sandbar / Shoal','Lock','Swamp')",
    "outputFields":["poigroup","poitype","poiname"],
    "outputCodeValueFields": ["poigroup"],
}
layer_info["poiLandform"] = {
    # Mountain peak, saddle, and other Landform points
    "layerName": "poiLandform",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poigroup = 7",
    "outputFields":["poigroup","poitype","poiname","poilabel","poilabeltype"],
    "outputCodeValueFields": ["poigroup"],
}
layer_info["geographicLine"] = {
    # Not using portal.spatial - look to replace with FuzzyExtentLine
    "layerName": "geographicLine",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/LPIMap/MapServer",
    "layer": "Ridge_Beach",
    "outputFields":["generalname","fuzzylinefeaturetype","relevance"],
    "outputCodeValueFields": ["fuzzylinefeaturetype"],
}
layer_info["placeLabel"] = {
    # placetype field is missing some Coded Values (23/11/23) - related style uses integers instead
    "layerName": "placeLabel",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Features_of_Interest_Category/MapServer/",
    "layer": "PlacePoint",
    "where": "generalname NOT LIKE '% HUT' AND generalname NOT LIKE '% SWAMP'",
    "outputFields":["generalname","placetype","relevance"],
    #"outputCodeValueFields": ["placetype"], 
}
layer_info["hydroAreaLabel"] = {
    "layerName": "hydroAreaLabel",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poitype IN ('Natural Waterbody','Manmade Waterbody','Bay / Inlet / Basin','Reach / River Bend')",
    "outputFields":["poitype","poiname"],
}
layer_info["hydroLineLabel"] = {
    "layerName": "hydroLineLabel",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Water_Theme/MapServer",
    "layer": "NamedWatercourse",
    "outputFields":["hydronamestring","relevance"],
}
layer_info["roadLabel"] = {
    # functionhierarchy field has no Coded Values (23/11/23) - related style uses integers instead
    "layerName": "roadLabel",
    "url": "https://portal.spatial.nsw.gov.au/server/rest/services/NSW_Transport_Theme/MapServer/",
    "layer": "RoadNameExtent",
    "where": "operationalstatus NOT IN (3,8) AND functionhierarchy NOT IN (7,10,11) AND (functionhierarchy NOT IN (6) OR relevance < 6) AND roadnamestring NOT LIKE '%BICENTENNIAL NATIONAL%' AND roadnamestring NOT LIKE '%AUSTRALIAN ALPS%' AND roadnameoid IS NOT NULL",
    "outputFields":["functionhierarchy","roadnamestring","relevance"],
    # "outputCodeValueFields": ["functionhierarchy"], 
}
layer_info["poiTransport"] = {
    # Places related to transports
    "layerName": "poiTransport",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poigroup = 4",
    "outputFields":["poigroup","poitype","poiname","poilabel","poilabeltype"],
    "outputCodeValueFields": ["poigroup"],
}
layer_info["poiCommunity"] = {
    # Community buildings, and homestead
    "layerName": "poiCommunity",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poigroup = 1",
    "outputFields":["poigroup","poitype","poiname","poilabel","poilabeltype"],
    "outputCodeValueFields": ["poigroup"],
}
layer_info["poiPlace"] = {
    # Unclear POI, it may be peculiar places
    "layerName": "poiPlace",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poigroup = 8",
    "outputFields":["poigroup","poitype","poiname","poilabel","poilabeltype"],
    "outputCodeValueFields": ["poigroup"],
}
layer_info["poiRecreation"] = {
    # Lookout, picnic point, other turistic points
    "layerName": "poiRecreation",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poigroup = 3",
    "outputFields":["poigroup","poitype","poiname","poilabel","poilabeltype"],
    "outputCodeValueFields": ["poigroup"],
}
layer_info["poiHydrography"] = {
    # Water related POI: waterfalls, dams, ...
    "layerName": "poiHydrography",
    "url": "https://maps.six.nsw.gov.au/arcgis/rest/services/sixmaps/POI/MapServer",
    "layer": "Points Of Interest",
    "where": "poigroup = 6",
    "outputFields":["poigroup","poitype","poiname","poilabel","poilabeltype"],
    "outputCodeValueFields": ["poigroup"],
}