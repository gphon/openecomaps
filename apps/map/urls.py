from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns( 'apps.map.views',

    url( r'^add$',                      'add_poi.add_poi' ),
    url( r'^edit/(?P<poi_id>\d*)$',     'edit_poi.edit_poi' ),
    url( r'^verify/(?P<poi_id>\d*)$',   'verify_poi.verify_poi' ),
    
    url( r'get/layer/(?P<layer>.*)',    'get_poi_layer.get_poi_layer' ),
)