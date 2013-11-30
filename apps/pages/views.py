from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi_filter import POIFilter
from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.seal_page import SealPage


def category_overview( request ):
    if request.session.has_key( 'last_visited_category' ):
        return overview_flyer( request, request.session['last_visited_category'] )
    else:
        categories = Category.objects.all().order_by( 'name' )
        return overview_flyer( request, categories[0] )
    #endif


def filter_overview( request ):
    if request.session.has_key( 'last_visited_filter' ):
        return overview_seals( request, request.session['last_visited_filter'] )
    else:
        #TODO: select id from database
        return overview_seals( request, 1 )
    #endif




def overview_flyer( request, category_id ):
    request.session['last_visited_category'] = category_id
    
    category = get_object_or_404( Category, id=category_id )
    pages = FlyerPage.objects.filter( category=category ).order_by( 'user__group_name' )
    page = None
    if request.user.is_authenticated():
        page = FlyerPage.objects.filter( user=request.user, category=category )
    context = {
        'selected' : category,
        'pages' : pages,
        'group_has_page' : page,
        'overview' : 'flyer',
    }
    return render_to_response( 'pages/overview.html', context,
                                    context_instance=RequestContext(request) )


def overview_seals( request, filter_id ):
    request.session['last_visited_filter'] = filter_id
    
    poi_filter = get_object_or_404( POIFilter, id=filter_id )
    pages = SealPage.objects.filter( filters=poi_filter )
    context = {
        'selected' : poi_filter,
        'pages' : pages,
        'overview' : 'seals',
    }
    return render_to_response( 'pages/overview.html', context,
                                    context_instance=RequestContext(request) )



def show_flyer_page( request, category_id, flyer_page_id ):
    category = get_object_or_404( Category, id=category_id )
    page = get_object_or_404( FlyerPage, category=category, id=flyer_page_id )
    context = {
        'selected' : category,
        'page' : page,
        'details' : 'flyer',
    }
    return render_to_response( 'pages/details_page.html', context,
                                    context_instance=RequestContext(request) )


def show_seal_page( request, filter_id, seal_page_id ):
    poi_filter = get_object_or_404( POIFilter, id=filter_id )
    page = get_object_or_404( SealPage, id=seal_page_id )
    context = {
        'selected' : poi_filter,
        'page' : page,
        'details' : 'seals',
    }
    return render_to_response( 'pages/details_page.html', context,
                                    context_instance=RequestContext(request) )