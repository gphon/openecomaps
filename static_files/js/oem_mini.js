var map;

/**
 * Function: initMap
 * Sets up the map, its layers and controls.
 * lat, lon, zoom are the initial map position, provided a permalink has not been used
 */
function initMap(lat, lon, zoom){
    map = new OpenLayers.Map(
                'map',
                {
                    maxExtent: new OpenLayers.Bounds( -20037508.34,-20037508.34,20037508.34,20037508.34 ),
                    numZoomLevels: 7,
                    maxResolution: 'auto',
                    units: 'm',
                    controls: [],
                    projection: new OpenLayers.Projection("EPSG:900913"),
                    displayProjection: new OpenLayers.Projection("EPSG:4326")
                }
            );
	
    OpenLayers.ImgPath = "/static/img/map/";
	
    var layerCloudMade = new OpenLayers.Layer.OSM(
                'Default map',
                [
                    "http://a.tile.cloudmade.com/8bafab36916b5ce6b4395ede3cb9ddea/27911/256/${z}/${x}/${y}.png",
                    "http://b.tile.cloudmade.com/8bafab36916b5ce6b4395ede3cb9ddea/27911/256/${z}/${x}/${y}.png",
                    "http://c.tile.cloudmade.com/8bafab36916b5ce6b4395ede3cb9ddea/27911/256/${z}/${x}/${y}.png"
                ],
                {
                    resolutions: [76.43702827148438, 38.21851413574219,19.109257067871095, 9.554628533935547, 4.777314266967774, 2.3886571, 1.1943286],
                    zoomOffset: 11,
                    numZoomLevels: 7
                }
            );
	var layerCycling = new OpenLayers.Layer.OSM(
				'Cycling map',
				[
					"http://a.tile.opencyclemap.org/cycle/${z}/${x}/${y}.png",
		         	"http://b.tile.opencyclemap.org/cycle/${z}/${x}/${y}.png",
		         	"http://c.tile.opencyclemap.org/cycle/${z}/${x}/${y}.png"
		         ],
				{
	  				resolutions: [76.43702827148438, 38.21851413574219, 19.109257067871095, 9.554628533935547, 4.777314266967774, 2.3886571, 1.1943286],
	  				zoomOffset: 11,
	  				numZoomLevels: 7,
					attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org">OpenStreetMap</a> and contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>.',
	  				buffer: 0
	  			}
	  		);
    var layerPublicTransport = new OpenLayers.Layer.OSM(
                'Public transport',
                [
                    "http://a.tile2.opencyclemap.org/transport/${z}/${x}/${y}.png",
                    "http://b.tile2.opencyclemap.org/transport/${z}/${x}/${y}.png",
                    "http://c.tile2.opencyclemap.org/transport/${z}/${x}/${y}.png"
                ],
                {
                    resolutions: [76.43702827148438, 38.21851413574219,19.109257067871095, 9.554628533935547, 4.777314266967774, 2.3886571, 1.1943286],
                    zoomOffset: 11,
                    numZoomLevels: 7,
                    attribution: 'Data, imagery and map information provided by <a href="http://www.openstreetmap.org">OpenStreetMap</a> and contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>.',
                    buffer: 0
                }
            );
    var layerAerial = new OpenLayers.Layer.Bing(
                {
                    name: "Aerial photography",
                    key: 'AoGQ41xJtaeTYW-5bGSuE7e589v03uKnxXeXmtFEsWMH1UoZMyhBydLItxE7Qua_',
                    type: 'Aerial'
                }
            );

    map.addLayers( [layerCloudMade, layerCycling, layerPublicTransport, layerAerial] );
    
  	
  	map.addControl(new OpenLayers.Control.PanZoomBar());
  	map.addControl(new OpenLayers.Control.Attribution());
  	map.addControl(new OpenLayers.Control.Navigation());
  	map.addControl(new OpenLayers.Control.Permalink());
    
    
    var layerSwitcherControl = new OpenLayers.Control.LayerSwitcher();
    map.addControl(layerSwitcherControl);
    layerSwitcherControl.maximizeControl();
    
/*  	
    var layerPower = addKMLLayer("Low carbon power", "http://www.openecomaps.co.uk/kml/one_planet_london/low_carbon_power.kml");
    var layerFood = addKMLLayer("Food", "http://www.openecomaps.co.uk/kml/one_planet_london/food.kml");
    var layerCulture = addKMLLayer("Culture and heritage", "http://www.openecomaps.co.uk/kml/one_planet_london/culture_and_heritage.kml");
    var layersPOI = [layerPower, layerFood, layerCulture];
    map.addLayers(layersPOI);
    var selectControl = new OpenLayers.Control.SelectFeature(layersPOI, {onSelect: onFeatureSelect, onUnselect: onFeatureUnselect});
    map.addControl(selectControl);
    selectControl.activate();

    var pack = gup('pack');
    script = document.createElement('script');
    script.src = '/script/map_packs.php?pack=' + pack;
    document.getElementsByTagName( 'head' )[0].appendChild(script);
*/  
  	
  	var lonLat = new OpenLayers.LonLat(lat, lon).transform(map.displayProjection,  map.projection);
  	map.setCenter (lonLat, zoom);
	
  	return map;
}



/*
 * Center the map on pack defaults if arguments haven't been passed in URL
 */
function center_map( lat, lon, zoom )
{  
  	if( !map.getCenter() ) {
    	var lonLat = new OpenLayers.LonLat(lon, lat).transform(map.displayProjection,  map.projection);
    	map.setCenter (lonLat, zoom);
  	}
}



/**
 * Function: addKMLLayer
 * Sets up a KML layer with popup classes
 * layername and layerurl are pretty self-explanatory
 */
function addKMLLayer(layername,layerurl)
{
    var kmllayer = new OpenLayers.Layer.GML(
                    layername,
                    layerurl,
                    {
                        format: OpenLayers.Format.KML,
                        projection: new OpenLayers.Projection("EPSG:4326"),
                        visibility: true,
                        formatOptions: {
                            extractStyles: true,
                            extractAttributes: true
                        }
                    } );
    return kmllayer;
}


function onPopupClose(evt)
{
//    selectControl.unselect(selectedFeature);
    onFeatureUnselect(selectedFeature);
}


function onFeatureSelect(feature)
{
    selectedFeature = feature;
    popup = new OpenLayers.Popup.FramedCloud(
                    'chicken',
                    feature.geometry.getBounds().getCenterLonLat(),
                    new OpenLayers.Size(100,100),
                    '<div><h3>' + feature.attributes.name + '</h3>' + feature.attributes.description + '</div>',
                    null,
                    true,
                    onPopupClose );
    feature.popup = popup;
    map.addPopup( popup );
}


function onFeatureUnselect(feature)
{
    if( feature.popup )
    {
        map.removePopup( feature.popup );
        feature.popup.destroy();
        feature.popup = null;
    }
}
