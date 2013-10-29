from django.conf.urls import patterns, url


urlpatterns  = patterns( 'apps.dummy_data.views',

    # ex: /dummy_data/create
    url( r'^create$',    'create_dummy_data' ),
    # ex: /dummy_data/show
    url( r'^show$',      'show_dummy_data' ),

)