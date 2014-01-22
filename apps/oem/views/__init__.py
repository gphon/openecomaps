import urllib.request


GOOGLE_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json?'


def get_data_from_google_api( values ):
    data = urllib.parse.urlencode( values )
    url = GOOGLE_API_URL + data
    resp = urllib.request.urlopen( url )
    html = resp.read()
    html = html.replace( b': true', b': True' )
    data = eval( html )
    return data