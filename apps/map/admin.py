from django.contrib import admin

from apps.map.models.area import Area
from apps.map.models.poi import POI
from apps.map.models.poi_filter import POIFilter


class AreaAdmin( admin.ModelAdmin ):
    pass

class POIAdmin( admin.ModelAdmin ):
    pass

class POIFilterAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Area, AreaAdmin )
admin.site.register( POI, POIAdmin )
admin.site.register( POIFilter, POIFilterAdmin )
