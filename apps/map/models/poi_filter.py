from django.db import models


class POIFilter( models.Model ):
    name = models.CharField( max_length=40 )
    
    def __str__( self ):
        return self.name
    
    class Meta:
        app_label = 'map'