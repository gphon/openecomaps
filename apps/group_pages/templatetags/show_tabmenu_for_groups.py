from django import template
from apps.group_pages.models.category import Category

register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_groups.html')
def show_tabmenu_for_groups( category_id, selected ):
    category = Category.objects.get( id=category_id )
    return {'category' : category, 'selected' : selected}