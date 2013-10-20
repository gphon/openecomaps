from django.contrib import admin

from models import Page
from models import PageCategory


class PageAdmin( admin.ModelAdmin ):
    pass

class PageCategoryAdmin( admin.ModelAdmin ):
    pass


admin.site.register( Page, PageAdmin )
admin.site.register( PageCategory, PageCategoryAdmin )