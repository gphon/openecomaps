from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns( '',
    
    url( r'^poi/',          include('apps.map.urls') ),
    url( r'^category/',     include('apps.group_pages.urls') ),
    url( r'^dummy_data/',   include('apps.dummy_data.urls') ),
    
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve' ),
    
    
    # ex: /
    url( r'^$',         TemplateView.as_view( template_name='home.html' ) ),
    # ex: /home
    url( r'^home$',     TemplateView.as_view( template_name='home.html' ) ),
    
    
    # ex: /overview
    url( r'^overview$',         'apps.auth.views.overview' ),
    # ex: /overview/poi
    url( r'^overview/poi$',     'apps.auth.views.overview_poi' ),
    # ex: /overview/pages
    url( r'^overview/pages$',   'apps.auth.views.overview_pages' ),
    
    
    # ex: /login
    url( r'^login$',    login,  {'template_name':'auth/auth.html'} ),
    # ex: /logout
    url( r'^logout$',   logout, {'next_page':'/home'} ),
    # ex: /settings
    url( r'^settings$', 'apps.auth.views.settings' ),
    
    
    # ex: /about
    url( r'^about$',     TemplateView.as_view( template_name='about.html' ) ),
    # ex: /copyrights
    url( r'^copyright$', TemplateView.as_view( template_name='copyright.html' ) ),
    # ex: /impressum
    url( r'^impressum$', TemplateView.as_view( template_name='impressum.html' ) ),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url( r'^admin/', include(admin.site.urls) ),
)
