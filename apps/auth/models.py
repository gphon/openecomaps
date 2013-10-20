from django.contrib.auth.models import User
from django.db import models

from apps.map.models import Area


class GPGroup( models.Model ):
    name  = models.CharField( max_length=50 )
    user = models.ForeignKey( User )
    
    areas = models.ManyToManyField( Area )
    
    def __str__( self ):
        return self.name
