from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi import AddPOIForm
from apps.map.views import get_data_from_google_api

import datetime


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
            """
            data = urllib.parse.urlencode( values )
            url = GOOGLE_API_URL + data
            resp = urllib.request.urlopen( url )
            data = eval( resp.read() )
            """
            data = get_data_from_google_api( values )
            #todo: if more than one result make a user request
            #todo; make sure that one result is minimum, else error
            coords = data['results'][0]['geometry']['location']
            poi.lat = coords['lat']
            poi.lon = coords['lng']
            poi.verified = False
            poi.verification_date = datetime.date.today()
            poi.save()
            #todo: check, that the id is not bigger than allowed
            #todo: get filter object and add this instead of any id
            for poi_filter in filters:
                poi.filters.add( poi_filter )
            for seal in seals:
                poi.seals.add( seal )
            #import pdb; pdb.set_trace()
            return HttpResponseRedirect( '/poi/add' )
    else:
        form = AddPOIForm()
    return render_to_response( 'poi_form.html', {'form' : form},
                                    context_instance=RequestContext(request) )