from django import template

register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_infopage.html')
def show_tabmenu_for_infopage( selected ):
    return {'selected' : selected}