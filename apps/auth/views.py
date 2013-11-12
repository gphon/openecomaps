from functools import reduce

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.auth.models.gp_group import GPGroup
from apps.map.models.poi import POI
from apps.pages.models.category import Category
from apps.map.models.poi_filter import POIFilter
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.flyer_page import FlyerPageForm

import operator


def overview( request ):
    if request.session.has_key( 'auth_overview' ):
        latest_auth_overview = request.session['auth_overview']
    else:
        latest_auth_overview = 'pois'
    #endif
    
    if   latest_auth_overview == 'pois':
        return overview_poi( request )
    elif latest_auth_overview == 'pages':
        return overview_pages( request )
    elif latest_auth_overview == 'settings':
        return settings( request )
    #endif


@login_required(login_url="/login")
def overview_poi( request ):
    request.session['auth_overview'] = 'pois'
    
    group = get_object_or_404( GPGroup, user=request.user )
    areas = group.areas.all()
    
    qset = [ Q( lat__range=(area.lat_bottom,area.lat_top) ) &
             Q( lon__range=(area.lon_left,area.lon_right) )
             for area in areas ]
    pois = POI.objects.filter( reduce( operator.or_, qset ) ).order_by( 'zip_code', 'name' )
    
    context = {
        'pois' : pois,
        'group' : group,
        'selected_page' : 'poi_overview',
    }
    return render_to_response( 'auth/overview_pois.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def overview_pages( request ):
    request.session['auth_overview'] = 'pages'
    
    group = get_object_or_404( GPGroup, user=request.user )
    categories = get_list_or_404( Category )
    
    entries = []
    for category in categories:
        page = FlyerPage.objects.filter( category=category, group=group )
        entries.append( ( page[0] if page else category ) )
    #endfor
    
    context = {
        'entries' : entries,
        'group' : group,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/overview_pages.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def settings( request ):
    request.session['auth_overview'] = 'settings'
    
    group = GPGroup.objects.get( user=request.user )
    
    context = {
        'group' : group,
        'selected_page' : 'settings_overview',
    }
    return render_to_response( 'auth/settings.html', context,
                                    context_instance=RequestContext(request) )




@login_required(login_url="/login")
def add_group_page( request, category_id ):
    group = get_object_or_404( GPGroup, user=request.user )
    category = get_object_or_404( Category, id=category_id )
    
    if request.method == 'POST':
        if request.POST.get( 'btn_add_page', '' ):
            # if page already exists, raise 404 error
            if FlyerPage.objects.filter( category_id=category_id, group=group ):
                raise Http404
            #endif
        #endif
        
        form = FlyerPageForm( request.POST )
        if form.is_valid():
            page = FlyerPage()
            page.title = form.cleaned_data['title']
            page.text = form.cleaned_data['text']
            page.image = form.cleaned_data['image']
            page.flyer = form.cleaned_data['flyer']
            page.group = group
            page.category = category
            
            page.save()
            
            return HttpResponseRedirect( '/overview' )
        #endif
    else:
        form = FlyerPageForm()
    #endif
    
    context = {
        'group' : group,
        'category' : category,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def edit_group_page( request, category_id ):
    group = get_object_or_404( GPGroup, user=request.user )
    category = get_object_or_404( Category, id=category_id )
    
    #: only if the page exist, we can edit it
    page = get_object_or_404( FlyerPage, category=category, group_id=group.id )
    
    form = FlyerPageForm( instance=page )
    if request.method == 'POST' and request.POST.get( 'btn_edit_page', '' ):
        form = FlyerPageForm( request.POST )
        if form.is_valid():
            print('blabla')
            form.save()
        #endif
    #endif
    
    context = {
        'group' : group,
        'category' : category,
        'page' : page,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def delete_group_page( request, category_id ):
    group = get_object_or_404( GPGroup, user=request.user )
    
    context = {
        'group' : group,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )