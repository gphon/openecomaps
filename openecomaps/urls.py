from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns( '',
    # ex: /
    url( r'^$',           'app_oem.views.home' ),
    # ex: /home/
    url( r'^home$',       'app_oem.views.home' ),
    
    # ex: /login/
    url( r'^login$',      'app_oem.views.info_view', {'template_name' : 'login.html'} ),
    # ex: /about/
    url( r'^about$',      'app_oem.views.info_view', {'template_name' : 'about.html'} ),
    # ex: /copyrights/
    url( r'^copyrights$', 'app_oem.views.info_view', {'template_name' : 'copyrights.html'} ),
    # ex: /impressum/
    url( r'^impressum$',  'app_oem.views.info_view', {'template_name' : 'impressum.html'} ),
    
    # ex: /search/berlin
    url( r'^search/(?P<search_term>.*)$',   'app_oem.views.search_view' ),
    
    # ex: /category/fish
    url( r'^category/(?P<category>.*)$',    'app_oem.views.category_overview' ),
    # ex: /category/fish/city/stuttgart
    url( r'^category/(?P<category>.*)/city/(?P<city>.*)$', 'app_oem.views.category_city' ),
    
    
    # ex: /add/poi/...
    url( r'^add/poi/(?P<data>.*)$',     'app_oem.views.add_poi' ),
    # ex: /del/poi/...
    url( r'^del/poi/(?P<data>.*)$',     'app_oem.views.del_poi' ),
    # ex: /update/poi/...
    url( r'^update/poi/(?P<data>.*)$',  'app_oem.views.update_poi_view' ),
    
    url( r'^fetch/pois/(?P<lon_left>.*)/(?P<lon_right>.*)/(?P<lat_top>.*)/(?P<lat_bottom>.*)$', 'app_oem.views.fetch_pois'),
    
    # ex: 
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve' ),


    # ex: /create_dummy_data/
    url( r'^create_dummy_data$', 'app_oem.tests.create_dummy_data_view' ),
    # ex: /show_dummy_data/
    url( r'^show_dummy_data$', 'app_oem.tests.show_dummy_data_view' ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url( r'^admin/', include(admin.site.urls) ),
)
