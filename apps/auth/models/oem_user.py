from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm

from apps.map.models.area import Area


class OEMUser( AbstractUser ):
    group_name = models.CharField( max_length=50 )
    areas = models.ManyToManyField( Area )
    
    def __str__( self ):
        return self.name
    
    class Meta:
        app_label = 'auth'


class OEMUserForm( ModelForm ):
    class Meta:
        model = OEMUser
        fields = ('password', )