import urllib


GOOGLE_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json?'


def fetch_poi_data_with_google_api( address ):
    data = urllib.parse.urlencode( { 'address' : address, 'sensor' : 'false' } )
    url = GOOGLE_API_URL + data
    try:
        resp = urllib.request.urlopen( url ).read()
        resp = resp.replace( b': true', b': True' )
        return eval( resp )
    except:
        return {}
    
    
def fetch_bounds_with_google_api( address ):
    json = fetch_poi_data_with_google_api( address )
    
    if not json:
        return {}
    
    bounds = json['results'][0]['geometry']['bounds']
    location = json['results'][0]['geometry']['location']
    
    return location

