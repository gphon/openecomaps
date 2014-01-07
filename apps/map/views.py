from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi import AddPOIForm
from apps.map.models.poi import POI
from apps.map.models.poi import POIForm

import datetime
import urllib.request


GOOGLE_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json?'


def home( request ):
    bounds = {
        "northeast" : { "lat" : 55.058347, "lng" : 15.0418961 },
        "southwest" : { "lat" : 47.2701114, "lng" : 5.8663425 }
    }
    location = {
        "lat" : 51.165691,
        "lng" : 10.451526,
    }
    zoom = 6
    if request.method == 'GET':
        query = request.GET.get( 'search-text', '' )
        if query:
            values = {
                'address' : query,
                'sensor' : 'false',
            }
            data = urllib.parse.urlencode( values )
            url = GOOGLE_API_URL + data
            resp = urllib.request.urlopen( url )
            data = eval( resp.read() )
            try:
                bounds = data['results'][0]['geometry']['bounds']
                location = data['results'][0]['geometry']['location']
                zoom = 11
            except:
                pass
    return render_to_response( 'home.html', {'home':True, 'bounds':str(bounds), 'location':str(location), 'zoom':zoom},
                                    context_instance=RequestContext(request) )



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
            out += '%s\t' % poi.text.replace( '/n', '<br>' )
            out += '/static/img/icons/%s.png\t' % layer # icon
            out += '25,25\t'                # iconSize
            out += '0,-16\n'                # iconOffset
        #endif
    #endfor
    return HttpResponse( out )


def add_poi( request ):
    if request.method == 'POST':
        form = AddPOIForm( request.POST )
        if form.is_valid():
            filters = form.cleaned_data['filters']
            seals = form.cleaned_data['seals']
            
            poi = form.save( commit=False )
            values = {
                'address' : poi.street + ',' + poi.zip_code + ',' + poi.city,
                'sensor' : 'false',
            }
            data = urllib.parse.urlencode( values )
            url = GOOGLE_API_URL + data
            resp = urllib.request.urlopen( url )
            data = eval( resp.read() )
            #todo: if more than one result make a user request
            #todo; make sure that one result is minimum, else error
            coords = data['results'][0]['geometry']['location']
            poi.lat = coords['lat']
            poi.lon = coords['lng']
            poi.verified = False
            poi.verification_date = datetime.date.today()
            poi.save()
            #todo: check, that the id is not bigger than allowed
            for poi_filter in filters:
                poi.filters.add( poi_filter )
            for seal in seals:
                poi.seals.add( seal )
            #import pdb; pdb.set_trace()
            return HttpResponse( 'add poi succeed' )
    else:
        form = AddPOIForm()
    return render_to_response( 'poi_form.html', {'form' : form},
                                    context_instance=RequestContext(request) )


@login_required(login_url="/login")
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