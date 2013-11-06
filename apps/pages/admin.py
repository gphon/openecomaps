from django.contrib import admin

from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.seal_page import SealPage


class CategoryAdmin( admin.ModelAdmin ):
    pass

class FlyerPageAdmin( admin.ModelAdmin ):
    pass

class SealPageAdmin( admin.ModelAdmin ):
    pass



admin.site.register( Category, CategoryAdmin )
admin.site.register( FlyerPage, FlyerPageAdmin )
admin.site.register( SealPage, SealPageAdmin )