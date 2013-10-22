from django import template
from apps.group_pages.models.category import Category

register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_categories.html')
def show_tabmenu_for_categories( selected ):
    categories = Category.objects.all()
    return {'categories' : categories, 'selected' : selected}