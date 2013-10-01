from django.conf.urls import patterns, include, url


urlpatterns = patterns( 'apps.map.views',

    url( r'^add$',      'add_poi' ),
    url( r'^del$',      'del_poi' ),
    url( r'^update$',   'update_poi' ),
    url( r'^verify$',   'verify_poi' ),
    url( r'^falsify$',  'falsify_poi' ),
    
    # ex: /fetch/12.885879,13.167087,52.512878,52.342996
    url( r'^fetchall/in/(?P<lon_left>.*),(?P<lat_bottom>.*),(?P<lon_right>.*),(?P<lat_top>.*)$', 'fetch_pois'),
    

)