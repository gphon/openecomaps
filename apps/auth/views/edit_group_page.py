from django.contrib.auth.decorators import login_required
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