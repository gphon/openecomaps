from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse

from apps.map.models.poi import POI


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