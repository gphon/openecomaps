from django.conf.urls import patterns, url


urlpatterns = patterns( 'apps.map.views',

    url( r'^add$',  'add_poi' ),
    url( r'^edit/(?P<poi_id>\d*)$',     'edit_poi' ),
    url( r'^verify/(?P<poi_id>\d*)$',   'verify_poi' ),
    
    url( r'get/layer/(?P<layer>.*)', 'get_poi_layer' ),

)
