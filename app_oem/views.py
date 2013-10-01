from django.shortcuts import render_to_response
from django.template import RequestContext




def home( request ):
    query = request.GET.get( 'search-text', '' )
    if query:
        pass
    return render_to_response( 'home.html',
                                    context_instance=RequestContext(request) )


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







def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}


