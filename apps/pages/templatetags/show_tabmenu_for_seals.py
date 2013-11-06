from django import template
from apps.map.models.poi_filter import POIFilter

register = template.Library()


@register.inclusion_tag('templatetags/tabmenu_for_seals.html')
def show_tabmenu_for_seals( selected ):
    poi_filters = POIFilter.objects.all()
    return {'filters' : poi_filters, 'selected' : selected}