from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.oem.models.area import Area


class OEMUser( AbstractUser ):
    group_name = models.CharField( max_length=50 )
    """
    office_street = models.CharField( max_length=50 )
    office_zip_code = models.CharField( max_length=50 )
    office_city = models.CharField( max_length=50 )
    """
    areas = models.ManyToManyField( Area )
    
    def __str__( self ):
        return self.group_name
    
    class Meta:
        app_label = 'auth'
        db_table = 'auth_user'