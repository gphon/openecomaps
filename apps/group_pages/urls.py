from django.conf.urls import patterns, url


urlpatterns = patterns( 'apps.group_pages.views',

    url( r'^(?P<category_id>\d*)$', 'category_overview' ),
    # ex: /category/4/show/city/17
    url( r'^(?P<category_id>\d*)/show/group/(?P<group_id>\d*)$', 'show_group_page' ),

)

urlpatterns += patterns( 'apps.auth.views',

    # ex: /category/4/add/city/17
    url( r'^(?P<category_id>\d*)/add$', 'add_group_page' ),
    # ex: /category/4/edit/city/17
    url( r'^(?P<category_id>\d*)/edit', 'edit_group_page' ),

)
