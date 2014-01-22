from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.oem.forms.oem_user import OEMUserChangeForm
from apps.oem.forms.oem_user import OEMUserCreationForm
from apps.oem.models.area import Area
from apps.oem.models.category import Category
from apps.oem.models.flyer_page import FlyerPage
from apps.oem.models.oem_user import OEMUser
from apps.oem.models.poi import POI
from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.seal_page import SealPage


class AreaAdmin( admin.ModelAdmin ):
    pass

class CategoryAdmin( admin.ModelAdmin ):
    pass

class FlyerPageAdmin( admin.ModelAdmin ):
    pass

class OEMUserAdmin( UserAdmin ):
    add_form = OEMUserCreationForm
    form = OEMUserChangeForm
    list_display = UserAdmin.list_display + ('date_joined', 'last_login')
    
    fieldsets = UserAdmin.fieldsets + (
            ( None, {'fields': ('group_name', 'areas')} ),
    )

class POIAdmin( admin.ModelAdmin ):
    pass

class POIFilterAdmin( admin.ModelAdmin ):
    pass

class SealPageAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Area, AreaAdmin )
admin.site.register( Category, CategoryAdmin )
admin.site.register( FlyerPage, FlyerPageAdmin )
admin.site.register( OEMUser, OEMUserAdmin )
admin.site.register( POI, POIAdmin )
admin.site.register( POIFilter, POIFilterAdmin )
admin.site.register( SealPage, SealPageAdmin )