from django import template

from apps.oem.models.category import Category


register = template.Library()


@register.inclusion_tag('templatetags/mainmenu_categories.html')
def show_mainmenu_categories():
    categories = Category.objects.all()
    return {'categories' : categories}