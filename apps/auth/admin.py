from django.contrib import admin

from models import GPGroup


class GPGroupAdmin( admin.ModelAdmin ):
    pass


admin.site.register( GPGroup, GPGroupAdmin )
