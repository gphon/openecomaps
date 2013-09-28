from django.shortcuts import render_to_response


def home_view( request ):
    return render_to_response( 'home.html' )


def info_view( request, template_name ):
    template_path = 'submenu/' + template_name
    return render_to_response( template_path )


def search_view( request, search_term ):
    # do something with the search term
    # load index page
    return render_to_response( 'home.html' )


def category_overview( request, category ):
    # check if category is valid
    return render_to_response( 'category.html', {'category': category} )

def category_city( request, category, city ):
    # check if category and city are valid
    data = {'category': category, 'city': city}
    return render_to_response( 'city_own_page.html', data )




def add_poi_view( request, data ):
    #:TODO
    return render_to_response( 'home.html' )

def del_poi_view( request, data ):
    #:TODO
    return render_to_response( 'home.html' )

def update_poi_view( request, data ):
    #:TODO
    return render_to_response( 'home.html' )

