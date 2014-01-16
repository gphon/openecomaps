from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi import POI
from apps.map.models.poi import POIForm


@login_required( login_url="/login" )
def edit_poi( request, poi_id ):
    poi = get_object_or_404( POI, id=poi_id )
    
    if request.method == 'POST':
        if request.POST.get('chk_del_1', '') and request.POST.get('chk_del_2', '') and request.POST.get('chk_del_3', ''):
            poi.delete()
            return HttpResponseRedirect( '/overview' )
        else:
            form = POIForm( request.POST, instance=poi )
            if form.is_valid():
                form.save()
            #endif
        #endif
    else:
        form = POIForm( instance=poi )
    #endif
    
    context = {
        'poi' : poi,
        'form' : form,
        'selected_page' : 'poi_overview',
    }
    return render_to_response( 'auth/edit_poi.html', context,
                                    context_instance=RequestContext(request) )