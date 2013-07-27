from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns( '',
    url( r'^$',           'app_map.views.home' ),
    url( r'^home$',       'app_map.views.home' ),
    
    url( r'^impressum$',  'views.info_view', {'template_name' : 'impressum.html'} ),
    url( r'^copyrights$', 'views.info_view', {'template_name' : 'copyrights.html'} ),
    url( r'^about$',      'views.info_view', {'template_name' : 'about.html'} ),
    
    
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve' ),


    url( r'^logo_pages/', include('app_logos.urls') ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url( r'^admin/', include(admin.site.urls) ),
)
