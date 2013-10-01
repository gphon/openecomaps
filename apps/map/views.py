from django.http import HttpResponse
from django.shortcuts import render_to_response

from app_oem.models import POI



def fetch_pois( request, lon_left, lon_right, lat_top, lat_bottom ):
    out = ''
    # fetch all POI's where lon_right > poi.lon > lon_left and where
    #                                           lat_top > poi.lat > lat_bottom
    for poi in POI.objects.filter( lon__gt=lon_left ).filter( lon__lt=lon_right ) \
                            .filter( lat__lt=lat_top ).filter( lat__gt=lat_bottom ):
        out += '%s\t' % poi.lat         # lat
        out += '%s\t' % poi.lon         # lon
        out += '%s\t' % poi.name        # title
        out += '%s\t' % poi.annotation  # description
        out += '%s\t' % 'blank'         # icon
        out += '%s\t' % '24,24'         # iconSize
        out += '%s\n' % '0,-16'         # iconOffset
    return HttpResponse( out[:-1] )


def add_poi( request ):
    text = ''
    for key, value in request.POST.items():
        text += '%s : %s<br>' % (key, value)
    return HttpResponse( text )

def del_poi( request ):
    #:TODO
    return render_to_response( 'home.html' )

def update_poi( request ):
    #:TODO
    return render_to_response( 'home.html' )

def verify_poi( request ):
    #:TODO
    pass

def falsify_poi( request ):
    #:TODO
    pass

