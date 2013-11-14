from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi import POI
from apps.map.models.poi import POIForm
from apps.auth.models.gp_group import GPGroup

import datetime


def get_poi_layer( request, layer ):
    try:
        koords = request.GET.get( 'bbox', '' )
        left, bottom, right, top = koords.split(',')
        lon_left, lon_right = float(left), float(right)
        lat_top, lat_bottom = float(top), float(bottom)
    except:
        raise Http404
    
    qset = Q(lon__gt=lon_left) & Q(lon__lt=lon_right) & Q(lat__lt=lat_top) & Q(lat__gt=lat_bottom)
    
    out = 'lat\tlon\ttitle\tdescription\ticon\ticonSize\ticonOffset\n'
    for poi in POI.objects.filter( qset ):
        if layer in [ poi_layer.name.lower() for poi_layer in poi.filters.all() ]:
            out += '%s\t%s\t' % ( poi.lat, poi.lon )
            out += '%s\t' % poi.name
            out += '%s\t' % poi.text
            out += '/static/img/icons/%s.png\t' % layer # icon
            out += '24,24\t'                # iconSize
            out += '0,-16\n'                # iconOffset
            print('%s - %s' % (layer, poi.name))
    print(out)
    return HttpResponse( out )


def add_poi( request ):
    text = ''
    for key, value in request.POST.items():
        text += '%s : %s<br>' % (key, value)
    return HttpResponse( text )


@login_required(login_url="/login")
def del_poi( request ):
    #TODO:
    return HttpResponseRedirect( '/overview/poi' )


@login_required(login_url="/login")
def edit_poi( request, poi_id ):
    group = get_object_or_404( GPGroup, user=request.user )
    poi = get_object_or_404( POI, id=poi_id )
    
    form = POIForm( instance=poi )
    if request.method == 'POST':
        form = POIForm( request.POST )
        if form.is_valid():
            form.save()
        #endif
    #endif
    context = {
        'group' : group,
        'poi' : poi,
        'form' : form,
    }
    return render_to_response( 'auth/edit_poi.html', context,
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
def verify_poi( request, poi_id ):
    poi = get_object_or_404( POI, id=poi_id )
    #TODO: check if access is allowed
    if poi.verified:
        poi.verified = False
    else:
        poi.verified = True
        poi.verification_date = datetime.date.today()
    poi.save()
    return HttpResponseRedirect( '/overview/poi' )