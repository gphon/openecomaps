from django.db import models


class POIFilter( models.Model ):
    name = models.CharField( max_length=40 )
    colour = models.CharField( max_length=7 )
    
    def __str__( self ):
        return self.name