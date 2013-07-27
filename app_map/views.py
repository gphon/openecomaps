from django.shortcuts import render_to_response
from models import City


def home( request ):
    query = request.GET.get( 'search-text', '' )
    if query:
        city = City.objects.get(name__contains=query)
        if not city:
            city = City.objects.get(name='Berlin')
    else:
        city = City.objects.get(name='Berlin')

    return render_to_response( 'home.html', {'city':city} )



def add_store( request ):
    pass

def del_store( request ):
    pass

def verify_store( request ):
    pass

def falsify_store( request ):
    pass
