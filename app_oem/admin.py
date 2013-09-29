from django.contrib import admin

from app_oem.models import Area
from app_oem.models import GPGroup
from app_oem.models import POI
from app_oem.models import POICategory
from app_oem.models import Seal


class AreaAdmin( admin.ModelAdmin ):
    pass

class GPGroupAdmin( admin.ModelAdmin ):
    pass

class POIAdmin( admin.ModelAdmin ):
    pass

class POICategoryAdmin( admin.ModelAdmin ):
    pass

class SealAdmin( admin.ModelAdmin ):
    pass



admin.site.register( Area, AreaAdmin )
admin.site.register( GPGroup, GPGroupAdmin )
admin.site.register( POI, POIAdmin )
admin.site.register( POICategory, POICategoryAdmin )
admin.site.register( Seal, SealAdmin )
