from django.db import models


class Area( models.Model ):
    name = models.CharField(max_length=50)
    
    # rectangle spread information
    lat_top     = models.FloatField()
    lat_bottom  = models.FloatField()
    lon_left    = models.FloatField()
    lon_right   = models.FloatField()
    
    def __eq__( self, other ):
        return self.id == other.id
    
    def __str__( self ):
        return '%s (%s/%s - %s/%s)' % ( self.name, self.lon_left, self.lat_top,
                                            self.lon_right, self.lat_bottom )
    
    class Meta:
        app_label = 'map'