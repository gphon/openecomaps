from django import template
from django.shortcuts import get_object_or_404

from apps.pages.models.seal_page import SealPage
from apps.map.models.poi_filter import POIFilter


register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_seal_page.html')
def show_tabmenu_for_seal_page( filter_id, selected ):
    print( 'filter_id: %s, selected: %s' % (filter_id, selected) )
    poi_filter = get_object_or_404( POIFilter, id=filter_id )
    pages = SealPage.objects.filter( filters=poi_filter )
    print( pages )
    return {'pages' : pages, 'selected' : selected}