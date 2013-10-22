from django.contrib import admin

from apps.group_pages.models.page import Page
from apps.group_pages.models.category import Category
from apps.group_pages.models.seal import Seal


class PageAdmin( admin.ModelAdmin ):
    pass

class CategoryAdmin( admin.ModelAdmin ):
    pass

class SealAdmin( admin.ModelAdmin ):
    pass



admin.site.register( Page, PageAdmin )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Seal, SealAdmin )