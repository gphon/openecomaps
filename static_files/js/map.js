var map;

function init(){
    map = new OpenLayers.Map('map');

    map.addLayer( new OpenLayers.Layer.OSM() );
    
    
    var layerFilterLebensmittel = new OpenLayers.Layer.Vector( "Lebensmittel",
        {
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            protocol: new OpenLayers.Protocol.HTTP(
                {
                    url : "/poi/get/layer/lebensmittel",
                    format : new OpenLayers.Format.Text()
                }
            )
        }
    );
    var layerFilterTextilien = new OpenLayers.Layer.Vector( "Textilien",
        {
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            protocol : new OpenLayers.Protocol.HTTP(
                {
                    url : "/poi/get/layer/textilien",
                    format: new OpenLayers.Format.Text()
                }
            )
        }
    );
    var layerFilterPapier = new OpenLayers.Layer.Vector( "Papier / Holz",
        {
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            protocol : new OpenLayers.Protocol.HTTP(
                {
                    url : "/poi/get/layer/papier_holz",
                    format: new OpenLayers.Format.Text()
                }
            )
        }
    );
    var layerFilterKosmetik = new OpenLayers.Layer.Vector( "Kosmetik",
        {
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            protocol : new OpenLayers.Protocol.HTTP(
                {
                    url : "/poi/get/layer/kosmetik",
                    format: new OpenLayers.Format.Text()
                }
            )
        }
    );
    var layerFilterMobilitaet = new OpenLayers.Layer.Vector( "Mobilität",
        {
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            protocol : new OpenLayers.Protocol.HTTP(
                {
                    url : "/poi/get/layer/mobilitaet",
                    format: new OpenLayers.Format.Text()
                }
            )
        }
    );
    var layerFilterSonstiges = new OpenLayers.Layer.Vector( "sonstiges",
        {
            strategies : [ new OpenLayers.Strategy.BBOX( {resFactor: 1.1} ) ],
            protocol : new OpenLayers.Protocol.HTTP(
                {
                    url : "/poi/get/layer/sonstiges",
                    format: new OpenLayers.Format.Text()
                }
            )
        }
    );
    
    
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
    
    
    map.addControl( new OpenLayers.Control.LayerSwitcher() );
    map.addControl( new OpenLayers.Control.PanZoomBar() );
    map.addControl( new OpenLayers.Control.Navigation() );
    
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