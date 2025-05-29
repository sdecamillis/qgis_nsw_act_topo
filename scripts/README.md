# nsw-act-topo

The project *nsw-act-topo* provides tools to build vector topographic maps for NSW and ACT in QGIS, using spatial data from [NSW Spatial Services](https://portal.spatial.nsw.gov.au/server/rest/services/), raster data for vegetation and hillshade, and possible additional features from [Open Street Map](https://www.openstreetmap.org)
It has been directly built from the [qgis-nsw-topo](https://github.com/tombrennan06/qgis-nsw-topo/) and [qgis-nsw-topo](https://github.com/mholling/nswtopo).

## Prerequisites

The *nsw-act-topo* scripts are designed to run on the software [QGIS](https://qgis.org/) (the project has been tested and developed on version 3.42.0).

Some optional data should be directly downloaded into your local machine:
* Raster tiles from the [TERN Data Discovery Portal](https://data.tern.org.au/rs/public/data/spot/woody_fpc_extent/nsw-2011/) for the woody extent and foliage projective cover (FPC) data,
* Digital Elevation Model (DEM) raster tiles from the [Elvis Elevation and Depth Portal](https://elevation.fsdf.org.au/) to generate hillshade effects.

## Content

The repo contains the following folders:
* *scrips*, containing all the Python scripts to be executed in the *Python Console* of QGIS;
* *models*, containing functions to be loaded and executed by the *Processing Toolbox* of QGIS;
* *topo_styles*, containing the QGIS style files for each imported layer;
* *svg*, containing QGIS-specific .svg files for custom markers;
* *templates*, containing templates for the map layout in QGIS.

## Usage

Here below a step-by-step description of how to use the tools of this project.

### Instaling QGIS and nsw-act-topo 

* Download and install the software [QGIS](https://qgis.org/). If you are new to this software, the [QGIS Documentation](https://docs.qgis.org/3.40/en/docs/user_manual/index.html) is a good starting point. If you want to learn more about QGIS and make custom changes to your maps, I would also recommand this [QGIS tutorial](https://www.qgistutorials.com/en/).
* [optional] under *Settings->Options->CRS* and *Transforms->Coordinate Transform* in QGIS, untick the option *Ask for datum transformation if several are available*. This is a recommended step to avoid the frequent prompts when accessing layer properties. The layers can be projected at later steps or at the map layout.
* [optional] if you wish to load the street layer from OpenStreetMaps as alternative layer to the NWS data, you first have to set up the processing modeler: in the *Processing Toolbox* of QGIS, load the model file located in the dedicated folder of the repository.
* Download the repository from Github into your local folder. You will make changes to your local copy of *nsw-act-topo*.

### Preliminary steps to create a new topo map

* Create a folder where you will store all the map data and your map project. Here, we will refer to this folder as working directory.
* Generate a vector layer (hereafter referred to as *extent*) providing the geographical boudaries of your map and place it in your working directory. The website [Ozultimate](https://maps.ozultimate.com) is a very handy solution. Draw a rectangle in the area of interest and save it as a GeoJSON file.
* [optional] If you wish to have a vegetation layer in the backgrond of your map, you can download the data from the [TERN Data Discovery Portal](https://data.tern.org.au/rs/public/data/spot/woody_fpc_extent/nsw-2011/). Download the _spot_nswgrs.zip_ file for the boundaries of all tiles and the specific tiles of interest (_s5hgps_rXXXcYYY_y20082012_bcvm6_r5m.img_).
* [optional] If you wish yo have hill-shade effects in the background of your map, you can download the elevation data from the [Elvis Elevation and Depth Portal](https://elevation.fsdf.org.au/). Follow the instruction on the wedsite (tip: you can use the extent file discussed above). [this functionality in the *nsw-act-topo* scripts is currently under development].
* In your *nsw-act-topo* folder, under the _scripts_ folder, update the file _local_settings.py_ with the following information: (a) the full path of your working directory, (b) the filename of the extent layer, (c) the directory containing the vegetation tiles (if any).

### Generating the topo map

Here the general instructions on how to use the *nsw-act-topo* script in QGIS:
* Open the *Python Console* (Ctrl+Alt+P), click *Show Editor* on the toolbar above the console, and open the file *main.py* by clicking the *Open Scripts* from the toolbar above the editor:
* Before proceeding, make sure to update the _local_settings.py_ file (see previous section).
* you can then click on *Run Script*. The extent boudary layer should appear in the QGIS window.
* In the *Python Console*, type the command `topo.vegetation` to load the vegetation layer (if any).
* Type the command `topo.layers` to fetch all the vector data intersecting the extent layer. Depending on the size of the area and the density of features, the script can take more than 5 minutes to complete. Urban areas will generally take longer than bush areas. The list of layers considered in this step are listed in the file *layer_list.py* under the *scripts* folder. You can modify such list to your preference.
* Type the command `topo.osmroad` to fetch the vector layer of roads from the OpenStreetMap server. You can then 
* This will fetch all the vector data intersecting the extent layer. Depending on the size of the area and the density of features, the script can take more than 5 minutes to complete. Urban areas will generally take longer than bush areas.

### Manual adjustments

* You can consider loading the road layer from OpenStreetMap by typing the command `topo.osmroad` in the Python Console. Then, you can tick or untick each sublayer from either the nsw_road or the osm_road layer.
* If you are familiar with QGIS, you can adjust style and labels.
* You can import your own layers directly into QGIS. For example, .gpx files with trails or points of interest.

### Saving layers and project

The vector layers fetched by the scripts are downloaded in a temporary folder. You can save them in your local project by typing `topo.save_layers` in the Python Console. All layers will be saved in a single .gpkg file.

Remember also to save the QGIS project, which will store all the custom styling options you introduced.

### Printing your map

To print your map, you have to create a map layout in *Project->New Print Layout*. After inserting the layout name, the new _layout_ window pops up. You can find online how to generate and save a map.
You can load a layout template under *layout->Add Items from template* and selecting one of the templates present in the repository.