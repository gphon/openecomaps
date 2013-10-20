from django import template
from apps.group_pages.models import PageCategory

register = template.Library()


@register.inclusion_tag('tabmenu_for_categories.html')
def show_tabmenu_for_categories( selected ):
    categories = PageCategory.objects.all()
    return {'categories' : categories, 'selected' : selected}