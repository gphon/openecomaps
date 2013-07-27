from django.conf.urls import patterns, include, url


urlpatterns = patterns( 'app_map.views',

    url( r'^add_store$',     'add_store' ),
    url( r'^del_store$',     'del_store' ),
    url( r'^verify_store$',  'verify_store' ),
    url( r'^falsify_store$', 'falsify_store' ),

)
