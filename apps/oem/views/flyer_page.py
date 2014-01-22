from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.oem.forms.flyer_page import FlyerPageForm
from apps.oem.models.category import Category
from apps.oem.models.flyer_page import FlyerPage
from apps.oem.models.oem_user import OEMUser

import datetime


@login_required(login_url="/login")
def add( request, category_id ):
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
def edit( request, category_id ):
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