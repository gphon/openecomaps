from django.shortcuts import render



def index( request ):
    query = request.GET.get( 'search-text', '' )
    if query:
        pass
    return render( 'index.html' )
