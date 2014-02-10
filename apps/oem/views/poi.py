from functools import reduce

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.oem.forms.poi import AddPOIForm
from apps.oem.forms.poi import EditPOIForm
from apps.oem.models.oem_user import OEMUser
from apps.oem.models.poi import POI
from apps.oem.views import get_data_from_google_api

import datetime
import operator


def add( request ):
    if request.method == 'POST':
        form = AddPOIForm( request.POST )
        if form.is_valid():
            poi = form.save( commit=False )
            
            values = {
                'address' : poi.street + ',' + poi.zip_code + ',' + poi.city,
                'sensor' : 'false',
            }
            """
            data = get_data_from_google_api( values )
            
            results = data['results']
            if not len( results ) == 1:
                form.errors['name'] = ['Kein Geschäft an dieser Adresse gefunden']
                return render_to_response( 'poi_form.html', {'form' : form},
                                    context_instance=RequestContext(request) )
            #end if
            
            has_street_number = False
            for item in results[0]['address_components']:
                if 'street_number' in item['types']:
                    has_street_number = True
                    break
                #end if
            #end for
            
            if not has_street_number:
                form.errors['name'] = ['Keine Hausnummer angegeben']
                return render_to_response( 'poi_form.html', {'form' : form},
                                    context_instance=RequestContext(request) )
            #end if
            
            coords = results[0]['geometry']['location']
            poi.lat = coords['lat']
            poi.lon = coords['lng']
            poi.save()
            
            for poi_filter in form.cleaned_data['filters']:
                poi.filters.add( poi_filter )
            for seal in form.cleaned_data['seals']:
                poi.seals.add( seal )
            """
            form.errors['name'] = 'Eintragung erfolgreich'
            return HttpResponseRedirect( '/poi/add' )
        #end if ( if form.is_valid() )
    else:
        form = AddPOIForm()
    #end if ( if request.method == 'POST' )
    
    return render_to_response( 'poi_form.html', {'form' : form},
                                    context_instance=RequestContext(request) )


@login_required( login_url="/login" )
def edit( request, poi_id ):
    poi = get_object_or_404( POI, id=poi_id )
    
    if request.method == 'POST':
        if request.POST.get('chk_del_1', '') and request.POST.get('chk_del_2', '') and request.POST.get('chk_del_3', ''):
            poi.delete()
            return HttpResponseRedirect( '/overview' )
        else:
            form = EditPOIForm( request.POST, instance=poi )
            if form.is_valid():
                form.save()
            #endif
        #endif
    else:
        form = EditPOIForm( instance=poi )
    #endif
    
    context = {
        'poi' : poi,
        'form' : form,
        'selected_page' : 'poi_overview',
    }
    return render_to_response( 'auth/edit_poi.html', context,
                                    context_instance=RequestContext(request) )


DESCRIPTION = '''
<table>
    <tr>
        <td>Öffnungszeiten:</td>
        <td>%(opening_time)s</td>
        <td rowspan="3"></td>
    </tr>
    <tr>
        <td>Webseite:</td>
        <td>%(website)s</td>
    </tr>
    <tr>
        <td>Beschreibung:</td>
        <td>%(description)s</td>
    </tr>
</table>\t'''

def get_layer( request, layer ):
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
            description_data = {
                'opening_time' : poi.opening_time,
                'website' : poi.website,
                'description' : poi.text.replace( '\n', '<br>' )
            }
            description = DESCRIPTION % description_data
            
            out += '%s\t%s\t' % ( poi.lat, poi.lon )
            out += '%s\t' % poi.name
            out += description.replace( '\n', '' )
            out += '/static/img/icons/%s.png\t' % layer # icon
            out += '25,25\t'                # iconSize
            out += '0,-16\n'                # iconOffset
        #endif
    #endfor
    return HttpResponse( out )


@login_required( login_url="/login" )
def verify( request, poi_id ):
    
    user = get_object_or_404( OEMUser, id=request.user.id )
    areas = user.areas.all()
    poi = get_object_or_404( POI, id=poi_id )
    
    if areas:
        qset = [ Q( lat__range=(area.lat_bottom,area.lat_top) ) &
                 Q( lon__range=(area.lon_left,area.lon_right) )
                 for area in areas ]
        pois = POI.objects.filter( reduce( operator.or_, qset ) )
    #end if
    
    # only if the poi is in my access area, one can verify it
    if poi in pois:
        if poi.verified:
            poi.verified = False
        else:
            poi.verified = True
            poi.verification_date = datetime.date.today()
        poi.save()
    #end if
    
    return HttpResponseRedirect( '/overview/poi' )
