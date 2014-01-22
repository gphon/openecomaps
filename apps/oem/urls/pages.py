from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns( 'apps.oem.views',
    
    # ex: /pages/category
    url( r'^category$',     'overviews.category_overview' ),
    # ex: /pages/filter
    url( r'^seals$',        'overviews.filter_overview' ),
    
    
    # ex: /pages/category/4
    url( r'^category/(?P<category_id>\d*)$',    'overviews.overview_flyer' ),
    # ex: /pages/filter/4
    url( r'^seals/(?P<filter_id>\d*)$',         'overviews.overview_seals' ),
    
    
    # ex: /pages/category/4/7
    url( r'^(?P<view>category)/(?P<item_id>\d*)/(?P<page_id>\d*)$', 'details_page.show_details_page' ),
    # ex: /pages/filter/4/11
    url( r'^(?P<view>seals)/(?P<item_id>\d*)/(?P<page_id>\d*)$',    'details_page.show_details_page' ),
    
    
    # ex: /pages/category/4/add
    url( r'^category/(?P<category_id>\d*)/add$',    'flyer_page.add' ),
    # ex: /pages/category/4/edit
    url( r'^category/(?P<category_id>\d*)/edit$',   'flyer_page.edit' ),

)