<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis labelsEnabled="0" version="3.42.0-Münster" readOnly="0" styleCategories="LayerConfiguration|Symbology|Labeling">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <renderer-v2 type="singleSymbol" forceraster="0" referencescale="-1" symbollevels="0" enableorderby="0">
    <symbols>
      <symbol type="marker" clip_to_extent="1" alpha="1" name="0" frame_rate="10" force_rhr="0" is_animated="0">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{79f62d7f-594c-4180-90d7-bf5a931f408d}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option type="QString" value="0" name="angle"/>
            <Option type="QString" value="square" name="cap_style"/>
            <Option type="QString" value="255,0,0,255,rgb:1,0,0,1" name="color"/>
            <Option type="QString" value="1" name="horizontal_anchor_point"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="line" name="name"/>
            <Option type="QString" value="0,0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="73,133,223,255,rgb:0.28627450980392155,0.52156862745098043,0.87450980392156863,1" name="outline_color"/>
            <Option type="QString" value="solid" name="outline_style"/>
            <Option type="QString" value="0.5" name="outline_width"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
            <Option type="QString" value="MM" name="outline_width_unit"/>
            <Option type="QString" value="diameter" name="scale_method"/>
            <Option type="QString" value="1.5" name="size"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
            <Option type="QString" value="MM" name="size_unit"/>
            <Option type="QString" value="1" name="vertical_anchor_point"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option type="Map" name="properties">
                <Option type="Map" name="angle">
                  <Option type="bool" value="true" name="active"/>
                  <Option type="QString" value="--checks if 'hydroLine' layer exists, and tries to use nearest segment angle&#xd;&#xa;--otherwise uses &quot;symbolrotation&quot; if !=0, or 0&#xd;&#xa;try(with_variable('hydroLine',overlay_nearest('hydroLine',@geometry)[0], line_interpolate_angle(@hydroLine,line_locate_point(@hydroLine,$geometry))-90),if(&quot;symbolrotation&quot;=0,0,&quot;symbolrotation&quot;-90))" name="expression"/>
                  <Option type="int" value="3" name="type"/>
                </Option>
              </Option>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
    <data-defined-properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </data-defined-properties>
  </renderer-v2>
  <selection mode="Default">
    <selectionColor invalid="1"/>
    <selectionSymbol>
      <symbol type="marker" clip_to_extent="1" alpha="1" name="" frame_rate="10" force_rhr="0" is_animated="0">
        <data_defined_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </data_defined_properties>
        <layer enabled="1" id="{5788f557-8ffc-4b87-8f7b-047ba02c8eb7}" pass="0" locked="0" class="SimpleMarker">
          <Option type="Map">
            <Option type="QString" value="0" name="angle"/>
            <Option type="QString" value="square" name="cap_style"/>
            <Option type="QString" value="255,0,0,255,rgb:1,0,0,1" name="color"/>
            <Option type="QString" value="1" name="horizontal_anchor_point"/>
            <Option type="QString" value="bevel" name="joinstyle"/>
            <Option type="QString" value="circle" name="name"/>
            <Option type="QString" value="0,0" name="offset"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
            <Option type="QString" value="MM" name="offset_unit"/>
            <Option type="QString" value="35,35,35,255,rgb:0.13725490196078433,0.13725490196078433,0.13725490196078433,1" name="outline_color"/>
            <Option type="QString" value="solid" name="outline_style"/>
            <Option type="QString" value="0" name="outline_width"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
            <Option type="QString" value="MM" name="outline_width_unit"/>
            <Option type="QString" value="diameter" name="scale_method"/>
            <Option type="QString" value="2" name="size"/>
            <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
            <Option type="QString" value="MM" name="size_unit"/>
            <Option type="QString" value="1" name="vertical_anchor_point"/>
          </Option>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </selectionSymbol>
  </selection>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style textOrientation="horizontal" fontSizeUnit="Point" forcedItalic="0" textColor="50,50,255,255,rgb:0.19607843137254902,0.19607843137254902,1,1" fontItalic="0" forcedBold="0" fontUnderline="0" fontKerning="1" legendString="Aa" fontWordSpacing="0" previewBkgrdColor="255,255,255,255,rgb:1,1,1,1" fontFamily="Arial" fontSizeMapUnitScale="3x:0,0,0,0,0,0" textOpacity="1" tabStopDistance="80" blendMode="0" namedStyle="Regular" tabStopDistanceUnit="Point" fieldName="generalname" isExpression="0" fontWeight="50" multilineHeightUnit="Percentage" fontSize="7" fontStrikeout="0" tabStopDistanceMapUnitScale="3x:0,0,0,0,0,0" allowHtml="0" useSubstitutions="0" multilineHeight="1" fontLetterSpacing="0" capitalization="0">
        <families/>
        <text-buffer bufferDraw="1" bufferSize="0.5" bufferNoFill="0" bufferJoinStyle="128" bufferSizeUnits="MM" bufferOpacity="1" bufferColor="255,255,255,255,rgb:1,1,1,1" bufferBlendMode="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
        <text-mask maskSize2="1.5" maskJoinStyle="128" maskSizeUnits="MM" maskType="0" maskedSymbolLayers="" maskEnabled="0" maskSize="1.5" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskOpacity="1"/>
        <background shapeType="0" shapeBlendMode="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeSizeType="0" shapeRotation="0" shapeFillColor="255,255,255,255,rgb:1,1,1,1" shapeSizeY="0" shapeJoinStyle="64" shapeRotationType="0" shapeRadiiUnit="Point" shapeDraw="0" shapeOffsetX="0" shapeBorderColor="128,128,128,255,rgb:0.50196078431372548,0.50196078431372548,0.50196078431372548,1" shapeRadiiX="0" shapeOffsetY="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="Point" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="Point" shapeOpacity="1" shapeBorderWidth="0" shapeOffsetUnit="Point" shapeRadiiY="0" shapeSVGFile="">
          <symbol type="marker" clip_to_extent="1" alpha="1" name="markerSymbol" frame_rate="10" force_rhr="0" is_animated="0">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" id="" pass="0" locked="0" class="SimpleMarker">
              <Option type="Map">
                <Option type="QString" value="0" name="angle"/>
                <Option type="QString" value="square" name="cap_style"/>
                <Option type="QString" value="141,90,153,255,rgb:0.55294117647058827,0.35294117647058826,0.59999999999999998,1" name="color"/>
                <Option type="QString" value="1" name="horizontal_anchor_point"/>
                <Option type="QString" value="bevel" name="joinstyle"/>
                <Option type="QString" value="circle" name="name"/>
                <Option type="QString" value="0,0" name="offset"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                <Option type="QString" value="MM" name="offset_unit"/>
                <Option type="QString" value="35,35,35,255,rgb:0.13725490196078433,0.13725490196078433,0.13725490196078433,1" name="outline_color"/>
                <Option type="QString" value="solid" name="outline_style"/>
                <Option type="QString" value="0" name="outline_width"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="outline_width_map_unit_scale"/>
                <Option type="QString" value="MM" name="outline_width_unit"/>
                <Option type="QString" value="diameter" name="scale_method"/>
                <Option type="QString" value="2" name="size"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="size_map_unit_scale"/>
                <Option type="QString" value="MM" name="size_unit"/>
                <Option type="QString" value="1" name="vertical_anchor_point"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
          <symbol type="fill" clip_to_extent="1" alpha="1" name="fillSymbol" frame_rate="10" force_rhr="0" is_animated="0">
            <data_defined_properties>
              <Option type="Map">
                <Option type="QString" value="" name="name"/>
                <Option name="properties"/>
                <Option type="QString" value="collection" name="type"/>
              </Option>
            </data_defined_properties>
            <layer enabled="1" id="" pass="0" locked="0" class="SimpleFill">
              <Option type="Map">
                <Option type="QString" value="3x:0,0,0,0,0,0" name="border_width_map_unit_scale"/>
                <Option type="QString" value="255,255,255,255,rgb:1,1,1,1" name="color"/>
                <Option type="QString" value="bevel" name="joinstyle"/>
                <Option type="QString" value="0,0" name="offset"/>
                <Option type="QString" value="3x:0,0,0,0,0,0" name="offset_map_unit_scale"/>
                <Option type="QString" value="MM" name="offset_unit"/>
                <Option type="QString" value="128,128,128,255,rgb:0.50196078431372548,0.50196078431372548,0.50196078431372548,1" name="outline_color"/>
                <Option type="QString" value="no" name="outline_style"/>
                <Option type="QString" value="0" name="outline_width"/>
                <Option type="QString" value="Point" name="outline_width_unit"/>
                <Option type="QString" value="solid" name="style"/>
              </Option>
              <data_defined_properties>
                <Option type="Map">
                  <Option type="QString" value="" name="name"/>
                  <Option name="properties"/>
                  <Option type="QString" value="collection" name="type"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadius="1.5" shadowRadiusAlphaOnly="0" shadowOffsetDist="1" shadowOffsetAngle="135" shadowBlendMode="6" shadowOffsetUnit="Point" shadowUnder="0" shadowRadiusUnit="Point" shadowOpacity="1" shadowOffsetGlobal="1" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowScale="100" shadowColor="0,0,0,255,rgb:0,0,0,1" shadowDraw="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0"/>
        <dd_properties>
          <Option type="Map">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format reverseDirectionSymbol="0" autoWrapLength="12" leftDirectionSymbol="&lt;" plussign="0" multilineAlign="3" rightDirectionSymbol=">" decimals="3" useMaxLineLengthForAutoWrap="1" placeDirectionSymbol="0" formatNumbers="0" addDirectionSymbol="0" wrapChar=""/>
      <placement offsetUnits="MM" centroidInside="0" rotationAngle="0" overrunDistance="0" preserveRotation="1" maximumDistance="0" repeatDistance="0" offsetType="1" repeatDistanceUnits="MM" quadOffset="4" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleOut="-25" geometryGeneratorType="PointGeometry" lineAnchorPercent="0.5" placement="6" xOffset="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" allowDegraded="0" maxCurvedCharAngleIn="25" distUnits="MM" polygonPlacementFlags="2" prioritization="PreferCloser" maximumDistanceMapUnitScale="3x:0,0,0,0,0,0" distMapUnitScale="3x:0,0,0,0,0,0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" yOffset="0" geometryGenerator="" centroidWhole="0" layerType="PointGeometry" lineAnchorTextPoint="FollowPlacement" lineAnchorClipping="0" priority="5" geometryGeneratorEnabled="0" lineAnchorType="0" fitInPolygonOnly="0" placementFlags="10" dist="0" overlapHandling="PreventOverlap" rotationUnit="AngleDegrees" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" maximumDistanceUnit="MM" overrunDistanceUnit="MM"/>
      <rendering scaleMax="0" obstacleFactor="1" zIndex="0" drawLabels="1" obstacle="1" upsidedownLabels="0" unplacedVisibility="0" minFeatureSize="0" fontMaxPixelSize="10000" fontLimitPixelSize="0" obstacleType="1" maxNumLabels="2000" fontMinPixelSize="3" limitNumLabels="0" scaleVisibility="0" mergeLines="0" labelPerPart="0" scaleMin="0"/>
      <dd_properties>
        <Option type="Map">
          <Option type="QString" value="" name="name"/>
          <Option name="properties"/>
          <Option type="QString" value="collection" name="type"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option type="QString" value="pole_of_inaccessibility" name="anchorPoint"/>
          <Option type="int" value="0" name="blendMode"/>
          <Option type="Map" name="ddProperties">
            <Option type="QString" value="" name="name"/>
            <Option name="properties"/>
            <Option type="QString" value="collection" name="type"/>
          </Option>
          <Option type="bool" value="false" name="drawToAllParts"/>
          <Option type="QString" value="0" name="enabled"/>
          <Option type="QString" value="point_on_exterior" name="labelAnchorPoint"/>
          <Option type="QString" value="&lt;symbol type=&quot;line&quot; clip_to_extent=&quot;1&quot; alpha=&quot;1&quot; name=&quot;symbol&quot; frame_rate=&quot;10&quot; force_rhr=&quot;0&quot; is_animated=&quot;0&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer enabled=&quot;1&quot; id=&quot;{d2084312-c7f1-4fce-a37c-cf929b33b3dd}&quot; pass=&quot;0&quot; locked=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;align_dash_pattern&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;square&quot; name=&quot;capstyle&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;5;2&quot; name=&quot;customdash&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;customdash_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;customdash_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;dash_pattern_offset&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;dash_pattern_offset_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;draw_inside_polygon&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;bevel&quot; name=&quot;joinstyle&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;60,60,60,255,rgb:0.23529411764705882,0.23529411764705882,0.23529411764705882,1&quot; name=&quot;line_color&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;solid&quot; name=&quot;line_style&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0.3&quot; name=&quot;line_width&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;line_width_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;offset&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;offset_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;offset_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;ring_filter&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;trim_distance_end&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_end_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;trim_distance_end_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;trim_distance_start&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;trim_distance_start_map_unit_scale&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;MM&quot; name=&quot;trim_distance_start_unit&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;0&quot; name=&quot;use_custom_dash&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot; name=&quot;width_map_unit_scale&quot;/>&lt;/Option>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option type=&quot;QString&quot; value=&quot;&quot; name=&quot;name&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option type=&quot;QString&quot; value=&quot;collection&quot; name=&quot;type&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>" name="lineSymbol"/>
          <Option type="double" value="0" name="minLength"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="minLengthMapUnitScale"/>
          <Option type="QString" value="MM" name="minLengthUnit"/>
          <Option type="double" value="0" name="offsetFromAnchor"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromAnchorMapUnitScale"/>
          <Option type="QString" value="MM" name="offsetFromAnchorUnit"/>
          <Option type="double" value="0" name="offsetFromLabel"/>
          <Option type="QString" value="3x:0,0,0,0,0,0" name="offsetFromLabelMapUnitScale"/>
          <Option type="QString" value="MM" name="offsetFromLabelUnit"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <previewExpression>"generalname"</previewExpression>
  <layerGeometryType>0</layerGeometryType>
</qgis>
