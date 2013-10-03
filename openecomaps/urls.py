from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns( '',
    
    url( r'^poi/', include('apps.map.urls') ),
    
    
    # ex: /
    url( r'^$',           'app_oem.views.home' ),
    # ex: /home/
    url( r'^home$',       'app_oem.views.home' ),
    
    
    # ex: /login/
    url( r'^login$',      'apps.auth.views.login' ),
    # ex: /logout/
    url( r'^logout$',     'apps.auth.views.logout' ),
    
    # ex: /overview/
    url( r'^overview$',   'apps.auth.views.overview' ),
    # ex: /overview/
    url( r'^overview/poi$',   'apps.auth.views.overview' ),
    # ex: /pages/
    url( r'^overview/pages$', 'apps.auth.views.pages' ),
    # ex: /about/
    url( r'^about$',      'apps.info_pages.views.info', {'template_name' : 'about'} ),
    # ex: /copyrights/
    url( r'^copyright$',  'apps.info_pages.views.info', {'template_name' : 'copyright'} ),
    # ex: /impressum/
    url( r'^impressum$',  'apps.info_pages.views.info', {'template_name' : 'impressum'} ),
    
    
    # ex: /search/berlin
    url( r'^search/(?P<search_term>.*)$',   'app_oem.views.search_view' ),
    
    
    # ex: /category/fish
    url( r'^category/(?P<category>.*)$',    'app_oem.views.category_overview' ),
    # ex: /category/fish/city/stuttgart
    url( r'^category/(?P<category>.*)/city/(?P<city>.*)$', 'app_oem.views.category_city' ),
    
    
    
    
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
