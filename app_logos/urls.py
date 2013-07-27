from django.conf.urls import patterns, include, url


urlpatterns = patterns( 'app_logos.views',

    url( r'^(?P<menu>.*)/(?P<tab>.*)$', 'logo_details' ),

)
