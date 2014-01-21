from django.conf.urls import patterns, url


urlpatterns  = patterns( 'apps.pages.views',

    # ex: /pages/category
    url( r'^category$', 'category_overview' ),
    # ex: /pages/filter
    url( r'^seals$',     'filter_overview' ),
    
    # ex: /pages/category/4
    url( r'^category/(?P<category_id>\d*)$',    'overview_flyer' ),
    # ex: /pages/filter/4
    url( r'^seals/(?P<filter_id>\d*)$',         'overview_seals' ),
    
    # ex: /pages/category/4/7
    url( r'^(?P<view>category)/(?P<item_id>\d*)/(?P<page_id>\d*)$', 'show_details_page' ),
    # ex: /pages/filter/4/11
    url( r'^(?P<view>seals)/(?P<item_id>\d*)/(?P<page_id>\d*)$',    'show_details_page' ),

)

urlpatterns += patterns( 'apps.auth.views',

    # ex: /category/4/add
    url( r'^category/(?P<category_id>\d*)/add$',    'add_group_page.add_group_page' ),
    # ex: /category/4/edit
    url( r'^category/(?P<category_id>\d*)/edit$',   'edit_group_page.edit_group_page' ),

)