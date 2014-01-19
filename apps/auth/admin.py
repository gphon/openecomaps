from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from apps.auth.models.oem_user import OEMUser


class OEMUserChangeForm( UserChangeForm ):
    class Meta( UserChangeForm.Meta ):
        model = OEMUser


class OEMUserAdmin( UserAdmin ):
    form = OEMUserChangeForm
    
    fieldsets = UserAdmin.fieldsets + (
            ( None, {'fields': ('group_name', 'areas')} ),
    )


admin.site.register( OEMUser, OEMUserAdmin )