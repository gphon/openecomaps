from django import template
from apps.group_pages.models import PageCategory

register = template.Library()


@register.inclusion_tag('mainmenu_categories.html')
def show_mainmenu_categories():
    categories = PageCategory.objects.all()
    return {'categories' : categories}