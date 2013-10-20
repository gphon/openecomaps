from django.contrib import admin

from models import Area
from models import POI
from models import POIFilter

class AreaAdmin( admin.ModelAdmin ):
    pass

class POIAdmin( admin.ModelAdmin ):
    pass

class POIFilterAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Area, AreaAdmin )
admin.site.register( POI, POIAdmin )
admin.site.register( POIFilter, POIFilterAdmin )
