from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Page
from models import PageCategory


def category_overview( request, category_id ):
    category = get_object_or_404( PageCategory, id=category_id )
    pages = Page.objects.filter( page_category=category )
    context = {
        'selected_category' : category,
        'pages' : pages,
    }
    return render_to_response( 'group_pages/category_overview.html', context,
                                    context_instance=RequestContext(request) )


def show_group_page( request, category_id, group_id ):
    category = get_object_or_404( PageCategory, id=category_id )
    page = get_object_or_404( Page, page_category=category, group_id=group_id )
    context = {
        'selected_category' : category,
        'page' : page,
    }
    return render_to_response( 'group_pages/group_page.html', context,
                                    context_instance=RequestContext(request) )


def add_group_page( request ):
    return render_to_response( '' )
