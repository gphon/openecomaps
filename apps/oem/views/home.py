from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.oem.views import get_data_from_google_api


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
            """
            data = urllib.parse.urlencode( values )
            url = GOOGLE_API_URL + data
            resp = urllib.request.urlopen( url )
            data = eval( resp.read() )
            """
            data = get_data_from_google_api( values )
            try:
                bounds = data['results'][0]['geometry']['bounds']
                location = data['results'][0]['geometry']['location']
                zoom = 11
            except:
                pass
    return render_to_response( 'home.html', {'home':True, 'bounds':str(bounds), 'location':str(location), 'zoom':zoom},
                                    context_instance=RequestContext(request) )