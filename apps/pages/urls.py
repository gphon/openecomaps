from django.conf.urls import patterns, url

urlpatterns  = patterns( 'apps.pages.views',

    # ex: /pages/category
    url( r'^category$', 'category_overview' ),
    # ex: /pages/filter
    url( r'^filter$',   'filter_overview' ),
    
    # ex: /pages/category/4
    url( r'^category/(?P<category_id>\d*)$',    'overview_flyer' ),
    # ex: /pages/filter/4
    url( r'^filter/(?P<filter_id>\d*)$',        'overview_seals' ),
    
    # ex: /pages/category/4/7
    url( r'^category/(?P<category_id>\d*)/(?P<flyer_page_id>\d*)$', 'show_flyer_page' ),
    # ex: /pages/filter/4/11
    url( r'^filter/(?P<filter_id>\d*)/(?P<seal_page_id>\d*)$',      'show_seal_page' ),

)

urlpatterns += patterns( 'apps.auth.views',

    # ex: /category/4/add
    url( r'^category/(?P<category_id>\d*)/add$',    'add_group_page' ),
    # ex: /category/4/edit
    url( r'^category/(?P<category_id>\d*)/edit$',   'edit_group_page' ),
    # ex: /category/4/del
    url( r'^category/(?P<category_id>\d*)/del$',    'delete_group_page' ),

)