"""
qgis-nsw-act-topo

This script is designed to build and manage topographic maps using QGIS.

This script:
1. Ensures that the required modules are available in the 'scripts' directory.
3. Instantiates the Topo_map_builder class with the repository directory path.
4. Imports and save layers.

Author: S De Camillis
Date: 29 May 2025
Version: 1.0
"""
import os
import sys
from PyQt5.QtCore import QSettings

# Add repository scirpt folder to path
repo_dir, _ = os.path.split(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(repo_dir, 'scripts'))

# Import modules from repository script folder
import qgis_functions as qf
import layer_list as ll
import local_settings as ls

def update_svg_search_paths(repo_dir):
        """Update the SVG search paths in QGIS settings."""
        qgis_settings = QSettings()
        svg_paths = qgis_settings.value("svg/searchPathsForSVG", [])
        svg_dir = os.path.join(repo_dir, 'svg')
        if svg_dir not in svg_paths:
            svg_paths.append(svg_dir)
            qgis_settings.setValue("svg/searchPathsForSVG", svg_paths)

class Topo_map_builder:
    def __init__(self, repo_dir):
        self.settings = ls.settings
        self.style_dir = os.path.join(repo_dir, 'topo_styles')

        # Set the svg path in QGIS
        update_svg_search_paths(repo_dir)

        # Load extent polygon layer
        qf.import_extent_layer(self.settings, self.style_dir)
    
    @property
    def vegetation(self):
        qf.import_vegetation_layer(self.settings, self.style_dir)
    
    @property
    def layers(self):
        qf.importQgisNwsTopoLayers(ll.layer_list, self.style_dir)
    
    @property
    def osmroad(self):
        qf.import_road_osm_layer(self.settings, self.style_dir)
        qf.relocate_above_another_layer('road_osm', 'road')
    
    @property
    def update_styles(self):
        qf.load_styles(self.style_dir)
    
    @property
    def save_layers(self):
        qf.save_vector_layers(self.settings)


topo = Topo_map_builder(repo_dir)