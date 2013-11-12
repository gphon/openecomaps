from django import forms

class LoginForm( forms.Form ):
    groupname = forms.CharField( max_length=50, label='Gruppe' )
    password = forms.CharField( max_length=32, label='Passwort', widget=forms.PasswordInput )