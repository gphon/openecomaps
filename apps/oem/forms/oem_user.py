from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from apps.oem.models.oem_user import OEMUser


class OEMUserChangeForm( UserChangeForm ):
    class Meta( UserChangeForm.Meta ):
        model = OEMUser


class OEMUserCreationForm( UserCreationForm ):
    class Meta( UserCreationForm.Meta ):
        model = OEMUser

    def clean_username( self ):
        username = self.cleaned_data['username']
        try:
            OEMUser.objects.get( username=username )
        except OEMUser.DoesNotExist:
            return username
        raise forms.ValidationError( self.error_messages['duplicate_username'] )