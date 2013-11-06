from django import template
from django.shortcuts import get_object_or_404

from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage


register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_flyer_page.html')
def show_tabmenu_for_flyer_page( category_id, selected_page_id ):
    category = get_object_or_404( Category, id=category_id )
    pages = FlyerPage.objects.filter( category=category ).order_by( 'group__name' )
    return {'pages' : pages, 'selected_page_id' : selected_page_id}