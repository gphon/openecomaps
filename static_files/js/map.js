var map;

function addLayer( layername, layerurl ) {
    var layer = new OpenLayers.Layer.Vector( layername, {
        // strategies: [ new OpenLayers.Strategy.Fixed() ],
        strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
        // projection: new OpenLayers.Projection( "EPSG:4326" ),
        // visibility: true,
        protocol: new OpenLayers.Protocol.HTTP( {
            url : layerurl,
            /*
            format : new OpenLayers.Format.KML( {
                extractStyles : true,
                extractAttributes : true,
            } )
            */
            format : new OpenLayers.Format.Text()
        } )
    } );
    return layer;
}


function init( bounds, location, zoom ) {
    map = new OpenLayers.Map( 'map', {
        controls: [
            new OpenLayers.Control.Navigation(),
            new OpenLayers.Control.PanZoomBar(),
            new OpenLayers.Control.LayerSwitcher(),
            new OpenLayers.Control.Permalink(),
            new OpenLayers.Control.ScaleLine(),
            new OpenLayers.Control.MousePosition(),
        ],
    } );

    map.addLayer( new OpenLayers.Layer.OSM() );
    
    var layerFilterLebensmittel = addLayer( "Lebensmittel", "/poi/get/layer/lebensmittel" );
    var layerFilterTextilien = addLayer( "Textilien", "/poi/get/layer/textilien" );
    var layerFilterPapier = addLayer( "Papier / Holz", "/poi/get/layer/papier_holz" );
    var layerFilterKosmetik = addLayer( "Kosmetik", "/poi/get/layer/kosmetik" );
    var layerFilterMobilitaet = addLayer( "Mobilität", "/poi/get/layer/mobilität" );
    var layerFilterSonstiges = addLayer( "sonstiges", "/poi/get/layer/sonstiges" );
    
    var layerMapAerial = new OpenLayers.Layer.Bing( {
        name : "Bing Map",
        key : 'AoGQ41xJtaeTYW-5bGSuE7e589v03uKnxXeXmtFEsWMH1UoZMyhBydLItxE7Qua_',
        type : 'Aerial'
    } );
    
    var apiKey = "AqTGBsziZHIJYYxgivLBf0hVdrAk9mWO5cQcb8Yux8sW5M8c8opEC2lZqKR1ZZXf";
    
    var layerMapRoad = new OpenLayers.Layer.Bing( {
        name: "Road",
        key: apiKey,
        type: "Road"
    } );
    
    var layerMapHybrid = new OpenLayers.Layer.Bing( {
        name: "Hybrid",
        key: apiKey,
        type: "AerialWithLabels"
    } );
/*    
    var aerial = new OpenLayers.Layer.Bing({
        name: "Aerial",
        key: apiKey,
        type: "Aerial"
    });
*/
    
    map.addLayers( [
        layerFilterLebensmittel,
        layerFilterPapier,
        layerFilterTextilien,
        layerFilterKosmetik,
        layerFilterMobilitaet,
        layerFilterSonstiges,
        layerMapAerial,
        layerMapRoad,
        layerMapHybrid
    ] );
    
    map.zoomToMaxExtent();
    
    selectControl = new OpenLayers.Control.SelectFeature(
        [
            layerFilterPapier,
            layerFilterLebensmittel
        ],
        {
            onSelect : onFeatureSelect,
            onUnselect: onFeatureUnselect
        }
    );
    map.addControl( selectControl );
    selectControl.activate();
    
    /*
    northeast = bounds["northeast"];
    southwest = bounds["southwest"];
    
    var bounds = new OpenLayers.Bounds();
    bounds.extend( new OpenLayers.LonLat( northeast["lng"], northeast["lat"] ) );
    bounds.extend( new OpenLayers.LonLat( southwest["lng"], southwest["lat"] ) );
    center = bounds.getCenterLonLat();
    
    var lonLat = new OpenLayers.LonLat( center.lon, center.lat ).transform(
        new OpenLayers.Projection("EPSG:4326"),
        map.getProjectionObject()
    );
    */
    var lonLat = new OpenLayers.LonLat( location["lng"], location["lat"] ).transform(
        new OpenLayers.Projection("EPSG:4326"),
        map.getProjectionObject()
    );
    map.setCenter( lonLat, zoom );
}


function onPopupClose( evt ) {
    onFeatureUnselect( selectedFeature );
}


function onFeatureSelect( feature ) {
    selectedFeature = feature;
    popup = new OpenLayers.Popup.FramedCloud(
        "chicken",
        feature.geometry.getBounds().getCenterLonLat(),
        new OpenLayers.Size(100,100),
        "<div><h3>"+feature.attributes.title+"</h3>"+feature.attributes.description+"</div>",
        null,
        true,
        onPopupClose
    );
    feature.popup = popup;
    map.addPopup(popup);
}


function onFeatureUnselect( feature ) {
    if( feature.popup ) {
        map.removePopup( feature.popup );
        feature.popup.destroy();
        feature.popup = null;
    }
}
