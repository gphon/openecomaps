from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.category import Category
from apps.oem.models.flyer_page import FlyerPage
from apps.oem.models.seal_page import SealPage


def show_details_page( request, view, item_id, page_id ):
    if view == 'category':
        selected = get_object_or_404( Category, id=item_id )
        page = get_object_or_404( FlyerPage, category=selected, id=page_id )
    elif view == 'seals':
        selected = get_object_or_404( POIFilter, id=item_id )
        page = get_object_or_404( SealPage, id=page_id )
    #endif
    context = {
        'selected' : selected,
        'page' : page,
        'view' : view,
    }
    return render_to_response( 'pages/details_page.html', context,
                                    context_instance=RequestContext(request) )