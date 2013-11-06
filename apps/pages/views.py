from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi_filter import POIFilter
from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.seal_page import SealPage


def category_overview( request ):
    if request.session.has_key( 'last_visited_category' ):
        last_visited_category_id = request.session['last_visited_category']
    else:
        last_visited_category_id = 1
        #TODO: select id from database
    #endif
    return overview_flyer( request, last_visited_category_id )


def filter_overview( request ):
    if request.session.has_key( 'last_visited_filter' ):
        last_visited_filter_id = request.session['last_visited_filter']
    else:
        last_visited_filter_id = 1
        #TODO: select id from database
    #endif
    return overview_seals( request, last_visited_filter_id )




def overview_flyer( request, category_id ):
    request.session['last_visited_category'] = category_id
    
    category = get_object_or_404( Category, id=category_id )
    pages = FlyerPage.objects.filter( category=category ).order_by( 'group__name' )
    page = None
    if request.user.is_authenticated():
        page = FlyerPage.objects.filter( group__user=request.user, category=category )
    context = {
        'selected' : category,
        'pages' : pages,
        'group_has_page' : page,
        'view' : 'flyer',
    }
    return render_to_response( 'pages/flyer_overview.html', context,
                                    context_instance=RequestContext(request) )


def overview_seals( request, filter_id ):
    request.session['last_visited_filter'] = filter_id
    
    poi_filter = get_object_or_404( POIFilter, id=filter_id )
    seals = SealPage.objects.filter( filters=poi_filter )
    context = {
        'selected' : poi_filter,
        'pages' : seals,
        'view' : 'seals',
    }
    return render_to_response( 'pages/seal_overview.html', context,
                                    context_instance=RequestContext(request) )



def show_flyer_page( request, category_id, flyer_page_id ):
    category = get_object_or_404( Category, id=category_id )
    page = get_object_or_404( FlyerPage, category=category, id=flyer_page_id )
    context = {
        'selected' : category,
        'page' : page,
        'view' : 'flyer',
    }
    return render_to_response( 'pages/flyer_page.html', context,
                                    context_instance=RequestContext(request) )


def show_seal_page( request, filter_id, seal_page_id ):
    poi_filter = get_object_or_404( POIFilter, id=filter_id )
    page = get_object_or_404( SealPage, id=seal_page_id )
    context = {
        'selected' : poi_filter,
        'page' : page,
        'view' : 'seals',
    }
    return render_to_response( 'pages/seal_page.html', context,
                                    context_instance=RequestContext(request) )