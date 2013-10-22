from django import template

from apps.group_pages.models import Category


register = template.Library()


@register.inclusion_tag('templatetags/mainmenu_categories.html')
def show_mainmenu_categories():
    categories = Category.objects.all()
    return {'categories' : categories}