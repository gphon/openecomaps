from django.http import HttpResponse
from django.shortcuts import render_to_response

from app_oem.models import POI



def home( request ):
    query = request.GET.get( 'search-text', '' )
    if query:
        pass
    return render_to_response( 'home.html' )


def info_view( request, template_name ):
    template_path = 'submenu/' + template_name
    return render_to_response( template_path )


def search_view( request, search_term ):
    # do something with the search term
    # load index page
    #:TODO
    return render_to_response( 'home.html' )


def category_overview( request, category ):
    # check if category is valid
    #:TODO
    return render_to_response( 'category.html', {'category': category} )


def category_city( request, category, city ):
    # check if category and city are valid
    #:TODO
    data = {'category': category, 'city': city}
    return render_to_response( 'city_own_page.html', data )


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


def add_poi( request, data ):
    #:TODO
    return render_to_response( 'home.html' )

def del_poi( request, data ):
    #:TODO
    return render_to_response( 'home.html' )

def update_poi_view( request, data ):
    #:TODO
    return render_to_response( 'home.html' )

def verify_store( request ):
    #:TODO
    pass

def falsify_store( request ):
    #:TODO
    pass