from functools import reduce

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.auth.models.oem_user import OEMUser
from apps.map.models.poi import POI
from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.flyer_page import FlyerPageForm

import datetime
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
    
    user = get_object_or_404( OEMUser, id=request.user.id )
    areas = user.areas.all()
    
    qset = [ Q( lat__range=(area.lat_bottom,area.lat_top) ) &
             Q( lon__range=(area.lon_left,area.lon_right) )
             for area in areas ]
    pois = POI.objects.filter( reduce( operator.or_, qset ) ).order_by( 'zip_code', 'name' )
    
    context = {
        'user' : user,
        'pois' : pois,
        'selected_page' : 'poi_overview',
    }
    return render_to_response( 'auth/overview_pois.html', context,
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
        'user' : user,
        'entries' : entries,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/overview_pages.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def settings( request ):
    request.session['auth_overview'] = 'settings'
    
    group = get_object_or_404( OEMUser, id=request.user.id )
    
    context = {
        'group' : group,
        'selected_page' : 'settings_overview',
    }
    return render_to_response( 'auth/settings.html', context,
                                    context_instance=RequestContext(request) )




@login_required(login_url="/login")
def add_group_page( request, category_id ):
    user = get_object_or_404( OEMUser, id=request.user.id )
    category = get_object_or_404( Category, id=category_id )
    
    if request.method == 'POST':
        # if page already exists, raise 404 error
        if FlyerPage.objects.filter( category_id=category_id, user=user ):
            raise Http404
        #endif
        
        form = FlyerPageForm( request.POST, request.FILES )
        if form.is_valid():
            # create, but don't save the instance
            page = form.save( commit=False )
            
            page.modified = datetime.datetime.now()
            page.user = user
            page.category = category
            
            page.save()
            return HttpResponseRedirect( '/overview' )
        #endif
    else:
        form = FlyerPageForm()
    #endif
    
    context = {
        'user' : user,
        'category' : category,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def edit_group_page( request, category_id ):
    user = get_object_or_404( OEMUser, id=request.user.id )
    category = get_object_or_404( Category, id=category_id )
    
    #: only if the page exist, we can edit it
    page = get_object_or_404( FlyerPage, category=category, user_id=user.id )
    
    if request.method == 'POST':
        if request.POST.get('chk_del_1', '') and request.POST.get('chk_del_2', '') and request.POST.get('chk_del_3', ''):
            page.delete()
            return HttpResponseRedirect( '/overview' )
        else:
            form = FlyerPageForm( request.POST, request.FILES, instance=page )
            if form.is_valid():
                page = form.save( commit=False )
                page.modified = datetime.datetime.now()
                page.save()
            #endif
        #endif
    else:
        form = FlyerPageForm( instance=page )
    #endif
    
    context = {
        'user' : user,
        'category' : category,
        'page' : page,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )