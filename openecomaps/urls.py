from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns( '',
    
    # ex: /
    url( r'^$',         'apps.oem.views.home.home' ),
    # ex: /home
    url( r'^home$',     'apps.oem.views.home.home' ),
    
    
    url( r'^admin/',    include( admin.site.urls ) ),
    url( r'^overview/', include( 'apps.oem.urls.overview' ) ),
    url( r'^pages/',    include( 'apps.oem.urls.pages' ) ),
    url( r'^poi/',      include( 'apps.oem.urls.poi' ) ),
    
    
    # ex: /login
    url( r'^login$',    login,  {'template_name':'auth/auth.html'} ),
    # ex: /logout
    url( r'^logout$',   logout, {'next_page':'/home'} ),
    
    
    # ex: /about
    url( r'^about$',     TemplateView.as_view( template_name='about.html' ) ),
    # ex: /copyrights
    url( r'^copyright$', TemplateView.as_view( template_name='copyright.html' ) ),
    # ex: /impressum
    url( r'^impressum$', TemplateView.as_view( template_name='impressum.html' ) ),
    
    
    # ex: /init
    url( r'^init$',      'apps.oem.init' ),
    # ex: /dummy_data/create
    url( r'^dummy_data/create$',    'apps.oem.dummy_data.views.create_dummy_data' ),
) + \
static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )