from django.conf.urls import patterns, url
from apps.group_pages import models

urlpatterns  = patterns( 'apps.group_pages.views',

    # ex: /category/4
    url( r'^(?P<category_id>\d*)$', 'category_overview' ),
    # ex: /category/4/flyer
    url( r'^(?P<category_id>\d*)/flyer$', 'category_overview_flyer' ),
    # ex: /category/4/flyer/7
    url( r'^(?P<category_id>\d*)/flyer/(?P<model_id>\d*)$', 'show_page', {'model':models.Page} ),
    #url( r'^(?P<category_id>\d*)/flyer/(?P<group_id>\d*)$', 'show_group_page' ),
    # ex: /category/4/seals/11
    url( r'^(?P<category_id>\d*)/seals/(?P<model_id>\d*)$', 'show_page', {'model':models.Seal} ),
    #url( r'^(?P<category_id>\d*)/seals/(?P<seal_id>\d*)$', 'show_seal_page' ),
    # ex: /category/4/seals
    url( r'^(?P<category_id>\d*)/seals$', 'category_overview_seals' ),
    
    
    # ex: /category/4/show/city/17
    url( r'^(?P<category_id>\d*)/show/group/(?P<group_id>\d*)$', 'show_group_page' ),

)

urlpatterns += patterns( 'apps.auth.views',

    # ex: /category/4/add
    url( r'^(?P<category_id>\d*)/add$',     'add_group_page' ),
    # ex: /category/4/edit
    url( r'^(?P<category_id>\d*)/edit$',    'edit_group_page' ),
    # ex: /category/4/del
    url( r'^(?P<category_id>\d*)/del$',     'delete_group_page' ),

)