from django.core.context_processors import csrf
from django.contrib import auth
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import Http404

from apps.auth.forms import LoginForm
from apps.auth.models.gp_group import GPGroup
from apps.group_pages.models import Category
from apps.group_pages.models.page import Page
from apps.group_pages.models.page import PageForm
from apps.map.models.poi import POI


from django.db.models import Q
import operator


def overview_poi( request ):
    if not request.user.is_authenticated():
        raise Http404
    
    request.session['overview'] = 'pois'
    
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


def overview_pages( request ):
    if not request.user.is_authenticated():
        raise Http404
    
    request.session['overview'] = 'pages'
    
    group = get_object_or_404( GPGroup, user=request.user )
    categories = get_list_or_404( Category )
    
    entries = []
    for category in categories:
        page = Page.objects.filter( category=category, group=group )
        entries.append( ( page[0] if page else category ) )
    #endfor
    
    context = {
        'entries' : entries,
        'group' : group,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/overview_pages.html', context,
                                    context_instance=RequestContext(request) )


def settings( request ):
    if not request.user.is_authenticated():
        raise Http404
    
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
    if not request.user.is_authenticated():
        raise Http404
    
    group = get_object_or_404( GPGroup, user=request.user )
    category = get_object_or_404( Category, id=category_id )
    
    if request.method == 'POST':
        if request.POST.get( 'btn_add_page', '' ):
            # if page already exists, raise 404 error
            if Page.objects.filter( category_id=category_id, group=group ):
                raise Http404
            #endif
        #endif
        
        form = PageForm( request.POST )
        if form.is_valid():
            page = Page()
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
        form = PageForm()
    #endif
    
    context = {
        'group' : group,
        'category' : category,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )


def edit_group_page( request, category_id ):
    if not request.user.is_authenticated():
        raise Http404
    group = get_object_or_404( GPGroup, user=request.user )
    category = get_object_or_404( Category, id=category_id )
    page = get_object_or_404( Page, category=category, group_id=group.id )
    form = PageForm( instance=page )
    context = {
        'group' : group,
        'category' : category,
        'page' : page,
        'form' : form,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/add_or_edit_page.html', context,
                                    context_instance=RequestContext(request) )


def delete_group_page( request, category_id ):
    if not request.user.is_authenticated():
        raise Http404
    
    group = get_object_or_404( GPGroup, user=request.user )
    
    context = {
        'group' : group,
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
