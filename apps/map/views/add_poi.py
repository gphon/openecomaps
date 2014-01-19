from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.map.models.poi import AddPOIForm
from apps.map.views import get_data_from_google_api


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
            data = get_data_from_google_api( values )
            
            num_results = len( data['results'] )
            if 0 < num_results < 2:
                coords = data['results'][0]['geometry']['location']
                poi.lat = coords['lat']
                poi.lon = coords['lng']
                poi.save()
                #todo: check, that the id is not bigger than allowed
                #todo: get filter object and add this instead of any id
                for poi_filter in filters:
                    poi.filters.add( poi_filter )
                for seal in seals:
                    poi.seals.add( seal )
                
                return HttpResponseRedirect( '/poi/add' )
            else:
                context = {
                    'form' : form,
                    'num_results' : num_results,
                }
                if num_results == 0:
                    pass
                else:
                    pass
                render_to_response( 'poi_form.html', context,
                                    context_instance=RequestContext(request) )
            #end if
    else:
        form = AddPOIForm()
    return render_to_response( 'poi_form.html', {'form' : form},
                                    context_instance=RequestContext(request) )