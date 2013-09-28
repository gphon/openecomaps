from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns( '',
    # ex: /
    url( r'^$',           'oem.views.home_view' ),
    # ex: /home/
    url( r'^home$',       'oem.views.home_view' ),
    
    # ex: /login/
    url( r'^login$',      'oem.views.info_view', {'template_name' : 'login.html'} ),
    # ex: /about/
    url( r'^about$',      'oem.views.info_view', {'template_name' : 'about.html'} ),
    # ex: /copyrights/
    url( r'^copyrights$', 'oem.views.info_view', {'template_name' : 'copyrights.html'} ),
    # ex: /impressum/
    url( r'^impressum$',  'oem.views.info_view', {'template_name' : 'impressum.html'} ),
    
    # ex: /search/berlin
    url( r'^search/(?P<search_term>.*)$',   'oem.views.search_view' ),
    
    # ex: /category/fish
    url( r'^category/(?P<category>.*)$',    'oem.views.category_overview' ),
    # ex: /category/fish/city/stuttgart
    url( r'^category/(?P<category>.*)/city/(?P<city>.*)$', 'oem.views.category_city' ),
    
    
    # ex: /add/poi/...
    url( r'^add/poi/(?P<data>.*)$',     'oem.views.add_poi_view' ),
    # ex: /del/poi/...
    url( r'^del/poi/(?P<data>.*)$',     'oem.views.del_poi_view' ),
    # ex: /update/poi/...
    url( r'^update/poi/(?P<data>.*)$',  'oem.views.update_poi_view' ),
    
    
    # ex: 
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve' ),


    # ex: 
    url( r'^logo_pages/', include('app_logos.urls') ),
    # ex: /create_dummy_data/
    url( r'^create_dummy_data$', 'oem.tests.create_dummy_data_view' ),
    # ex: /show_dummy_data/
    url( r'^show_dummy_data$', 'oem.tests.show_dummy_data_view' ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url( r'^admin/', include(admin.site.urls) ),
)
