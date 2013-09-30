import hashlib

from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from app_oem.forms import LoginForm

from app_oem.models import GPGroup
from app_oem.models import POI



def home( request ):
    query = request.GET.get( 'search-text', '' )
    if query:
        pass
    return render_to_response( 'home.html' )



def login( request ):
    context = {}
    context.update( csrf(request) )
    
    if request.method == 'POST':
        form = LoginForm( request.POST )
        if form.is_valid():
            groupname = form.cleaned_data['groupname']
            password = hashlib.md5( form.cleaned_data['password'] ).hexdigest()
            
            try:
                group = GPGroup.objects.get( name__iexact=groupname, password=password )
                request.session['group_id'] = group.id
            except GPGroup.DoesNotExist:
                pass
            
            if request.user.is_authenticated():
                pass
            else:
                pass
        #endif
    else:
        form = LoginForm()
    #endif
    
    context['form'] = form
    if request.session['group_id']:
        context['login'] = True
    return render_to_response( 'login.html', context,
                                    context_instance=RequestContext(request) )


def logout( request ):
    try:
        del request.session['group_id']
    except KeyError:
        pass
    return render_to_response( 'home.html' )


def info_view( request, template_name ):
    return render_to_response( template_name )


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


def add_poi( request ):
    text = str( request )
    return render_to_response( text )

def del_poi( request ):
    #:TODO
    return render_to_response( 'home.html' )

def update_poi( request ):
    #:TODO
    return render_to_response( 'home.html' )

def verify_store( request ):
    #:TODO
    pass

def falsify_store( request ):
    #:TODO
    pass
