from django import forms
from django.forms import ModelForm

from apps.oem.models.oem_user import OEMUser


class ChangeSettingsForm( ModelForm ):
    password  = forms.CharField( max_length=32, label='Passwort (alt)', widget=forms.PasswordInput, required=False )
    password1 = forms.CharField( max_length=32, label='Passwort (neu)', widget=forms.PasswordInput, required=False )
    password2 = forms.CharField( max_length=32, label='Passwort (wdh)', widget=forms.PasswordInput, required=False )
    
    def clean_password2( self ):
        if self.data['password1'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        else:
            raise forms.ValidationError( 'Passwords do not match.' )
        #end if
    
    class Meta:
        model = OEMUser
        fields = ('email',)
        labels = {
            'email' : 'E-Mail',
        }