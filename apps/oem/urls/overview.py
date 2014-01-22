from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns( 'apps.oem.views',
    
    # ex: /overview
    url( r'^$',             'overviews.overview' ),
    # ex: /overview/poi
    url( r'^poi$',          'overviews.overview_pois' ),
    # ex: /overview/pages
    url( r'^pages$',        'overviews.overview_pages' ),
    # ex: /overview/settings
    url( r'^settings$',     'overviews.overview_settings' ),

)