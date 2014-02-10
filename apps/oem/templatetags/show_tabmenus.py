from django import template
from django.shortcuts import get_object_or_404

from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.category import Category
from apps.oem.models.flyer_page import FlyerPage
from apps.oem.models.seal_page import SealPage


register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_overview.html')
def show_tabmenu_for_overview( tabmenu, selected ):
    if   tabmenu == 'category':
        tabs = Category.objects.all()
    elif tabmenu == 'seals':
        tabs = POIFilter.objects.all()
    return {'tabmenu' : tabmenu, 'tabs' : tabs, 'selected' : selected}


@register.inclusion_tag('templatetags/tabmenu_for_details_page.html')
def show_tabmenu_for_details_page( tabmenu, tab_id, selected ):
    if   tabmenu == 'category':
        category = get_object_or_404( Category, id=tab_id )
        tabs = FlyerPage.objects.filter( category=category ).order_by( 'user__group_name' )
        return {'tabmenu' : tabmenu, 'tabs' : tabs, 'menu' : category, 'selected' : selected}
    else:
        poi_filter = get_object_or_404( POIFilter, id=tab_id )
        tabs = SealPage.objects.filter( filters=poi_filter )
        return {'tabmenu' : tabmenu, 'tabs' : tabs, 'menu' : poi_filter, 'selected' : selected}