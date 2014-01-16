from django import forms


class LoginForm( forms.Form ):
    groupname = forms.CharField( max_length=50, label='Gruppe' )
    password = forms.CharField( max_length=32, label='Passwort', widget=forms.PasswordInput )


class ChangeSettingsForm( forms.Form ):
    passward1 = forms.CharField( max_length=32, label='Passwort (neu)', widget=forms.PasswordInput )
    passward2 = forms.CharField( max_length=32, label='Passwort (wdh)', widget=forms.PasswordInput )
    
    class Meta:
        model = 