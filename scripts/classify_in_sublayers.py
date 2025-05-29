from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsCategorizedSymbolRenderer,
    QgsRendererCategory,
    QgsSymbol
)
from qgis.utils import iface

# Set your layer name and field name here
layer_name = "highway"
field_name = "highway"

# Get the layer by its name
layer = QgsProject.instance().mapLayersByName(layer_name)
if not layer:
    print(f"Layer '{layer_name}' not found.")
    exit()

layer = layer[0]

# Check if the field exists
if field_name not in [field.name() for field in layer.fields()]:
    print(f"Field '{field_name}' not found in layer '{layer_name}'.")
    exit()

# Get unique values for the field
unique_values = layer.uniqueValues(layer.fields().indexFromName(field_name))

# Create categories
categories = []
for value in unique_values:
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor.fromHsv(hash(value) % 360, 200, 255))  # Generate unique color for each value
    category = QgsRendererCategory(value, symbol, str(value))
    categories.append(category)

# Create and apply renderer
renderer = QgsCategorizedSymbolRenderer(field_name, categories)
layer.setRenderer(renderer)
layer.triggerRepaint()

# Add the layer to the Layers panel if it's not already loaded
if not QgsProject.instance().layerTreeRoot().findLayer(layer.id()):
    QgsProject.instance().addMapLayer(layer)

iface.mapCanvas().refresh()

print(f"Sublayers categorized by '{field_name}' successfully created.")