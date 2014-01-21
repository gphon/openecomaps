from functools import reduce

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.auth.forms import ChangeSettingsForm
from apps.auth.models.oem_user import OEMUser
from apps.map.models.poi import POI
from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage

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
    
    qset = [ Q( lat__range=(area.lat_bottom,area.lat_top) ) &
             Q( lon__range=(area.lon_left,area.lon_right) )
             for area in areas ]
    pois = POI.objects.filter( reduce( operator.or_, qset ) ).order_by( 'zip_code', 'name' )
    
    context = {
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
        'entries' : entries,
        'selected_page' : 'pages_overview',
    }
    return render_to_response( 'auth/overview_pages.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def overview_settings( request ):
    request.session['auth_overview'] = 'settings'
    user = get_object_or_404( OEMUser, id=request.user.id )
    
    if request.method == 'POST':
        form = ChangeSettingsForm( request.POST, instance=user )
        
        if form.is_valid():
            user = form.save( commit=False )
            password = form.cleaned_data['password']
            if password:
                if user.check_password( password ):
                    password1 = form.cleaned_data['password1']
                    if password1:
                        new_password = form.clean_password2()
                        user.set_password( new_password )
                        user.save()
                    else:
                        form.errors['password1'] = ['New password must not be empty']
                    #end if
                else:
                    form.errors['password'] = ['Password incorrect']
                #end if
            #end if
        #end if
    else:
        form = ChangeSettingsForm( instance=user )
    
    context = {
        'form' : form,
        'selected_page' : 'settings_overview',
    }
    return render_to_response( 'auth/overview_settings.html', context,
                                    context_instance=RequestContext(request) )