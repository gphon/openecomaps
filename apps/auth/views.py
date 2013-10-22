from django.core.context_processors import csrf
from django.contrib import auth
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from apps.auth.forms import LoginForm
from apps.auth.models.gp_group import GPGroup
from apps.group_pages.models import Category
from apps.group_pages.models.page import Page
from apps.group_pages.models.page import PageForm
from apps.map.models.poi import POI


def overview_poi( request ):
    request.session['overview'] = 'pois'
    
    if request.POST:
        pass
    
    group = get_object_or_404( GPGroup, user=request.user )
    areas = group.areas.all()
    pois = set( [] )
    for area in areas:
        queryset = POI.objects.filter( lat__range=(area.lat_bottom,area.lat_top),
                                       lon__range=(area.lon_left,area.lon_right) )
        pois |= set( queryset )
    #endfor
    
    context = {
        'pois' : list( pois ),
        'group' : group,
        'selected_page' : 'poi_overview',
    }
    return render_to_response( 'auth/overview_pois.html', context,
                                    context_instance=RequestContext(request) )


def overview_pages( request ):
    request.session['overview'] = 'pages'
    
    group = get_object_or_404( GPGroup, user=request.user )
    categories = Category.objects.all()
    
    entry_list = []
    for category in categories:
        page = Page.objects.filter( category=category, group=group )
        entry_list.append( ( page[0] if page else category ) )
    #endfor
    context = {
        'entries' : entry_list,
        'group' : group,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/overview_pages.html', context,
                                    context_instance=RequestContext(request) )


def settings( request ):
    request.session['overview'] = 'settings'
    
    group = GPGroup.objects.get( user=request.user )
    context = {
        'group' : group,
        'selected_page' : 'settings_overview',
    }
    return render_to_response( 'auth/settings.html', context,
                                    context_instance=RequestContext(request) )


def overview( request ):
    if request.session.has_key( 'overview' ):
        latest_overview_page = request.session['overview']
    else:
        latest_overview_page = 'pois'
    #endif
    
    if   latest_overview_page == 'pois':
        return overview_poi( request )
    elif latest_overview_page == 'pages':
        return overview_pages( request )
    elif latest_overview_page == 'settings':
        return settings( request )
    #endif





def add_group_page( request, category_id ):
    group = get_object_or_404( GPGroup, user=request.user )
    form = PageForm()
    context = {
        'group' : group,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )


def edit_group_page( request, category_id ):
    group = get_object_or_404( GPGroup, user=request.user )
    category = get_object_or_404( Category, id=category_id )
    page = get_object_or_404( Page, category=category, group_id=group.id )
    form = PageForm( instance=page )
    context = {
        'group' : group,
        'page' : page,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )



def login( request ):
    if request.method == 'POST':
        form = LoginForm( request.POST )
        if form.is_valid():
            groupname = form.cleaned_data['groupname'].lower()
            password = form.cleaned_data['password']
            
            user = auth.authenticate( username=groupname, password=password )
            if user is not None and user.is_active:
                auth.login( request, user )
                return HttpResponseRedirect( '/overview' )
            #endif
        #endif
    else:
        form = LoginForm()
    #endif
    
    context = { 'form' : form }
    context.update( csrf(request) )
    return render_to_response( 'auth/auth.html', context,
                                    context_instance=RequestContext(request) )


def logout( request ):
    auth.logout( request )
    return render_to_response( 'home.html' )
