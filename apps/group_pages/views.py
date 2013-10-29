from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.group_pages.models.page import Page
from apps.group_pages.models.seal import Seal
from apps.group_pages.models.category import Category


def category_overview( request, category_id ):
    #TODO: decide if overview flyer or overview seal
    return category_overview_flyer( request, category_id )


def category_overview_flyer( request, category_id ):
    category = get_object_or_404( Category, id=category_id )
    pages = Page.objects.filter( category=category ).order_by( 'group__name' )
    page = None
    if request.user.is_authenticated():
        page = Page.objects.filter( group__user=request.user, category=category )
    context = {
        'selected_category' : category,
        'pages' : pages,
        'group_has_page' : page,
    }
    return render_to_response( 'group_pages/category_overview.html', context,
                                    context_instance=RequestContext(request) )


def category_overview_seals( request, category_id ):
    #TODO: show page for a seal
    return category_overview_flyer( request, category_id )


"""
merge show group page and show seal page
"""
def show_page( request, category_id, model, model_id ):
    category = get_object_or_404( Category, id=category_id )
    page = get_object_or_404( model, category=category, group_id=model_id )
    context = {
        'selected_category' : category,
        'page' : page,
    }
    return render_to_response( 'group_pages/group_page.html', context,
                                    context_instance=RequestContext(request) )

"""
def show_group_page( request, category_id, group_id ):
    category = get_object_or_404( Category, id=category_id )
    page = get_object_or_404( Page, category=category, group_id=group_id )
    context = {
        'selected_category' : category,
        'page' : page,
    }
    return render_to_response( 'group_pages/group_page.html', context,
                                    context_instance=RequestContext(request) )


def show_seal_page( request, category_id, seal_id ):
    category = get_object_or_404( Category, id=category_id )
    seal = get_object_or_404( Seal, category=category, group_id=seal_id )
    context = {
        'selected_category' : category,
        'page' : seal,
    }
    return render_to_response( 'group_pages/group_page.html', context,
                                    context_instance=RequestContext(request) )
"""