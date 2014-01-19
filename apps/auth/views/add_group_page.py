from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.auth.models.oem_user import OEMUser
from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.flyer_page import FlyerPageForm

import datetime


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