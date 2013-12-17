var map;

function addLayer( layername, layerurl )
{
    var layer = new OpenLayers.Layer.Vector( layername,
        {
            // strategies: [ new OpenLayers.Strategy.Fixed() ],
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            // projection: new OpenLayers.Projection( "EPSG:4326" ),
            // visibility: true,
            protocol: new OpenLayers.Protocol.HTTP(
                {
                    url : layerurl,
                    /*
                    format : new OpenLayers.Format.KML(
                        {
                            extractStyles : true,
                            extractAttributes : true,
                        }
                    )
                    */
                    format : new OpenLayers.Format.Text()
                }
            )
        }
    );
    return layer;
}


function init(){
    map = new OpenLayers.Map(
        'map',
        {
            controls: [
                new OpenLayers.Control.Navigation(),
                new OpenLayers.Control.PanZoomBar(),
                new OpenLayers.Control.LayerSwitcher(),
                new OpenLayers.Control.ScaleLine(),
                new OpenLayers.Control.OverviewMap(),
            ],
        }
    );

    map.addLayer( new OpenLayers.Layer.OSM() );
    
    var layerFilterLebensmittel = addLayer( "Lebensmittel", "/poi/get/layer/lebensmittel" );
    var layerFilterTextilien = addLayer( "Textilien", "/poi/get/layer/textilien" );
    var layerFilterPapier = addLayer( "Papier / Holz", "/poi/get/layer/papier_holz" );
    var layerFilterKosmetik = addLayer( "Kosmetik", "/poi/get/layer/kosmetik" );
    var layerFilterMobilitaet = addLayer( "Mobilität", "/poi/get/layer/mobilitaet" );
    var layerFilterSonstiges = addLayer( "sonstiges", "/poi/get/layer/sonstiges" );
    
    var layerMapAerial = new OpenLayers.Layer.Bing(
        {
            name : "Bing Map",
            key : 'AoGQ41xJtaeTYW-5bGSuE7e589v03uKnxXeXmtFEsWMH1UoZMyhBydLItxE7Qua_',
            type : 'Aerial'
        }
    );
    
    
    map.addLayers(
        [
            layerFilterLebensmittel,
            layerFilterPapier,
            layerFilterTextilien,
            layerFilterKosmetik,
            layerFilterMobilitaet,
            layerFilterSonstiges,
            layerMapAerial
        ]
    );
    
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
    
    
    var lonLat = new OpenLayers.LonLat( 13.053131,52.403257 ).transform(
        new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
        map.getProjectionObject()               // to Spherical Mercator Projection
    );
    var zoom=12;
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
    if( feature.popup )
    {
        map.removePopup( feature.popup );
        feature.popup.destroy();
        feature.popup = null;
    }
}