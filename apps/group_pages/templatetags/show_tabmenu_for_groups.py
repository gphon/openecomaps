from django import template
from django.shortcuts import get_object_or_404

from apps.group_pages.models.category import Category
from apps.group_pages.models.page import Page


register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_groups.html')
def show_tabmenu_for_groups( category_id, selected ):
    category = get_object_or_404( Category, id=category_id )
    pages = Page.objects.filter( category=category ).order_by( 'group__name' )
    return {'pages' : pages, 'selected' : selected}