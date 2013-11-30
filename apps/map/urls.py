from django.conf.urls import patterns
from django.conf.urls import url
from django.views.generic.base import TemplateView
from apps.map.models.poi import AddPOIForm


urlpatterns = patterns( 'apps.map.views',

    url( r'^add$',  'add_poi' ),
    url( r'^edit/(?P<poi_id>\d*)$',     'edit_poi' ),
    url( r'^verify/(?P<poi_id>\d*)$',   'verify_poi' ),
    
    url( r'^form$', TemplateView.as_view( template_name='poi_form.html' ), {'form':AddPOIForm()} ),
    
    url( r'get/layer/(?P<layer>.*)', 'get_poi_layer' ),

)
