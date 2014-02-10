from functools import reduce

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.oem.forms.change_settings import ChangeSettingsForm
from apps.oem.models.category import Category
from apps.oem.models.flyer_page import FlyerPage
from apps.oem.models.oem_user import OEMUser
from apps.oem.models.poi import POI
from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.seal_page import SealPage

import operator


def overview( request ):
    if request.session.has_key( 'auth_overview' ):
        latest_auth_overview = request.session['auth_overview']
    else:
        latest_auth_overview = 'pois'
    #endif
    
    if   latest_auth_overview == 'pois':
        return overview_pois( request )
    elif latest_auth_overview == 'pages':
        return overview_pages( request )
    elif latest_auth_overview == 'settings':
        return overview_settings( request )
    #endif


@login_required(login_url="/login")
def overview_pois( request ):
    request.session['auth_overview'] = 'pois'
    
    user = get_object_or_404( OEMUser, id=request.user.id )
    areas = user.areas.all()
    
    if areas:
        qset = [ Q( lat__range=(area.lat_bottom,area.lat_top) ) &
                 Q( lon__range=(area.lon_left,area.lon_right) )
                 for area in areas ]
        pois = POI.objects.filter( reduce( operator.or_, qset ) ).order_by( 'zip_code', 'name' )
    else:
        pois = []
    
    context = {
        'pois' : pois,
        'selected' : 'poi_overview',
    }
    return render_to_response( 'intern/overview_pois.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def overview_pages( request ):
    request.session['auth_overview'] = 'pages'
    
    user = get_object_or_404( OEMUser, id=request.user.id )
    categories = get_list_or_404( Category )
    
    entries = []
    for category in categories:
        page = FlyerPage.objects.filter( category=category, user=user )
        entries.append( ( page[0] if page else category ) )
    #endfor
    
    context = {
        'entries' : entries,
        'selected' : 'pages_overview',
    }
    return render_to_response( 'intern/overview_pages.html', context,
                                    context_instance=RequestContext(request) )


from django.contrib.auth.forms import PasswordChangeForm


@login_required(login_url="/login")
def overview_settings( request ):
    request.session['auth_overview'] = 'settings'
    user = get_object_or_404( OEMUser, id=request.user.id )
    
    if request.method == 'POST':
        form = ChangeSettingsForm( request.POST, instance=user )
        
        if form.is_valid():
            user = form.save()
        #end if
    else:
        form = ChangeSettingsForm( instance=user )
    
    context = {
        'form' : form,
        'selected' : 'settings',
    }
    return render_to_response( 'intern/overview_settings.html', context,
                                    context_instance=RequestContext(request) )




def category_overview( request ):
    if request.session.has_key( 'last_visited_category' ):
        return overview_flyer( request, request.session['last_visited_category'] )
    else:
        categories = Category.objects.all().order_by( 'name' )
        category = categories[0]
        return overview_flyer( request, category.id )
    #endif


def filter_overview( request ):
    if request.session.has_key( 'last_visited_filter' ):
        return overview_seals( request, request.session['last_visited_filter'] )
    else:
        poi_filters = POIFilter.objects.all().order_by('id')
        poi_filter = poi_filters[0]
        return overview_seals( request, poi_filter.id )
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
        'view' : 'category',
    }
    return render_to_response( 'pages/overview.html', context,
                                    context_instance=RequestContext(request) )


def overview_seals( request, filter_id ):
    print( filter_id )
    request.session['last_visited_filter'] = filter_id
    print( filter_id )
    poi_filter = get_object_or_404( POIFilter, id=filter_id )
    pages = SealPage.objects.filter( filters=poi_filter )
    context = {
        'selected' : poi_filter,
        'pages' : pages,
        'view' : 'seals',
    }
    print( context )
    return render_to_response( 'pages/overview.html', context,
                                    context_instance=RequestContext(request) )