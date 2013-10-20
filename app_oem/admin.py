from django.contrib import admin

from app_oem.models import Seal


class SealAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Seal, SealAdmin )
