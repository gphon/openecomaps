from django.shortcuts import render_to_response
from django.template import RequestContext

import urllib
from socket import timeout
from apps.oem.views import fetch_bounds_with_google_api


def home( request ):
    
    if request.method == 'GET':
        query = request.GET.get( 'search-text', '' )
        if query:
            zoom = 11
            bounds = fetch_bounds_with_google_api( query )
        
        elif False:
            #TODO: check if cookie for bounds is set
            #TODO: if true, take this data else
            pass
        
        else:
            #: fetch remote adress
            remote_address = request.META.get('REMOTE_ADDR')
            
            #: use freeGeoIP API to get the current city of the user
            url = 'http://freegeoip.net/json/' + remote_address
            
            #: try to get api request and fetch the current city
            #: if timeout do nothing (default value is used)
            try:
                resp = urllib.request.urlopen( url, timeout=2 )
                json = eval( resp.read().decode('utf-8') )
                if json['city']:
                    address = json['city']
                    zoom = 11
                else:
                    address = 'Germany'
                    zoom = 6
            except timeout:
                print( 'socket timed out - URL %s', url )
                address = 'Germany'
                zoom = 6
            
            #: get the map data from google maps for the given city
            bounds = fetch_bounds_with_google_api( address )
    
    context = {
        'home':True,
        'bounds':str(bounds),
        'location':str(bounds),
        'zoom':zoom
    }
    return render_to_response( 'home.html', context,
                                    context_instance=RequestContext(request) )