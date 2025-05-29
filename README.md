# qgis-nsw-osm-topo

This project provides tools to build vector topographic maps for NSW and ACT in QGIS, using spatial data from [NSW Spatial Services](https://portal.spatial.nsw.gov.au/server/rest/services/) and [Open Street Map](https://www.openstreetmap.org), and additional raster data for vegetation and hillshade.
It has been directly built from the [qgis-nsw-topo](https://github.com/tombrennan06/qgis-nsw-topo/).

## Prerequisites

The following software is required in order to run the script of *qgis-nsw-osm-topo*:
* The [QGIS](https://qgis.org/) software (the project has been tested and developed on version 3.42.0).

Some optional data should be directly downloaded into your local machine:
* Raster tiles from the [TERN Data Discovery Portal](https://data.tern.org.au/rs/public/data/spot/woody_fpc_extent/nsw-2011/) for the woody extent and foliage projective cover (FPC) data,
* Digital Elevation Model (DEM) raster tiles from the [Elvis Elevation and Depth Portal](https://elevation.fsdf.org.au/) to generate hillshade effects.

## Content

The repo contains the following folders:
* *scrips*, containing all the Python scripts to be executed in the *Python Console* of QGIS;
* *models*, containing functions to be loaded and executed by the *Processing Toolbox* of QGIS;
* *styles*, containing the QGIS style files for each imported layer;
* *svg*, containing QGIS-specific .svg files for custom markers;
* *templates*, containing templates for the map layout in QGIS.

## Usage

Here below a step-by-step description of how to use the tools of this project.

### Setting up QGIS

After downloading and installing QGIS, action the following steps:
* under *Settings->Options->System* in QGIS, add the path of the SVG files to the *SVG Paths* box.
* under *Settings->Options->CRS and Transforms->Coordinate Transform* in QGIS, untick the option 'Ask for datum transformation if several are available'. This is not a required step, but it is recommended to avoid several prompts while working with layers. The layers can be projected at later steps.
* [optional] loading the models in the *Processing Toolbox* of QGIS

### Gathering initial data

Create your project folder and gather the following data:
* an extent layer defining the boudaries of your map. The website [Ozultimate](https://maps.ozultimate.com) is a very handy solution. Draw a rectangle in the area of interest and save it as a GeoJSON file.
* [optional] the vegetation layer from the [TERN Data Discovery Portal](https://data.tern.org.au/rs/public/data/spot/woody_fpc_extent/nsw-2011/). Download the _spot_nswgrs.zip_ file for the boundaries of all tiles and the specific tiles of interest (_s5hgps_rXXXcYYY_y20082012_bcvm6_r5m.img_).
* [optional] the DEM layer(s)

### Generating the topo map

Here the general instructions on how customise and execute the python script in QGIS:
* Open the *Python Console* (Ctrl+Alt+P), click *Show Editor* on the toolbar above the console, and open the file *generate_map.py* by clicking the *Open Scripts* from the toolbar above the editor:
* Update the _localParams_ section with the following information: 1) your project directory (absolute path), 2) the filename of the extent layer, 2) [optional] the directory (absolute path) where you store the vegetation tiles and the _spot_nswgrs.zip_ boundary file.
* you can click on *Run Script*. This will fetch all the vector data within the extent layer. Depending on the size of the area and the density of information, the script can take more than 5 minutes to complete. Urban areas will generally take longer than bush areas.

### Manual adjustments

If you are familiar with QGIS, you can adjust style and labels.
* You can consider loading the road layer from osm by executing the _run_highway_model_ section of the script directly in the qgis python console. Therefore, you can tick or untick each sublayer from either the nsw_road or the osm_road layer.
* You can import additional layers directly into QGIS. For example, .gpx files with trails or points of interest.

### Saving layers and project

If you have included additional layers, you have to save them in your local project folder. Simply, execute the _save_vector_layers_ section of the script directly in the qgis python console. All layers will be saved in a single .gpkg file.

Remember to save the QGIS project, which will store all the custom styling options you introduced.

### Printing your map

To print your map, you have to create a map layout in *Project->New Print Layout*. After inserting the layout name, the new _layout_ window pops up. You can find online how to generate and save a map.

You can load a layout template under *layout->Add Items from template* and selecting one of the templates present in the repository.
