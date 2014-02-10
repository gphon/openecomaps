from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns( 'apps.oem.views',
    
    # ex: /poi/get/layer/lebensmittel
    url( r'^get/layer/(?P<layer>.*)',   'poi.get_layer' ),
    
    # ex: /poi/add
    url( r'^add$',                      'poi.add',      name='add_poi' ),
    # ex: /poi/edit/5
    url( r'^edit/(?P<poi_id>\d*)$',     'poi.edit' ),
    # ex: /poi/verify/7
    url( r'^verify/(?P<poi_id>\d*)$',   'poi.verify' ),

)