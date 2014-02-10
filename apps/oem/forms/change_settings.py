from django.forms import ModelForm

from apps.oem.models.oem_user import OEMUser


class ChangeSettingsForm( ModelForm ):
    class Meta:
        model = OEMUser
        fields = ('email',)
        labels = {
            'email' : 'E-Mail',
        }