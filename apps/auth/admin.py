from django.contrib import admin

from apps.auth.models.gp_group import GPGroup


class GPGroupAdmin( admin.ModelAdmin ):
    pass


admin.site.register( GPGroup, GPGroupAdmin )
