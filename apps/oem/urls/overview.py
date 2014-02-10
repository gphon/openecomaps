from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib.auth.views import password_change


urlpatterns = patterns( 'apps.oem.views',
    
    # ex: /overview
    url( r'^$',             'overviews.overview' ),
    # ex: /overview/poi
    url( r'^poi$',          'overviews.overview_pois' ),
    # ex: /overview/pages
    url( r'^pages$',        'overviews.overview_pages' ),
    # ex: /overview/settings
    url( r'^settings$',     'overviews.overview_settings' ),
    # ex: /overview/settings/password_change
    url( r'^settings/password_change', password_change,
                        { 'template_name':'intern/password_change.html',
                          'post_change_redirect':'/overview/settings',
                          'extra_context' : {'selected':'settings'} } ),

)