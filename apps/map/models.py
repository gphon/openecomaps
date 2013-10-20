from django.db import models

from app_oem.models import Seal


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


class POIFilter( models.Model ):
    name = models.CharField( max_length=40 )
    colour = models.CharField( max_length=7 )
    
    def __str__( self ):
        return self.name


class POI( models.Model ):
    name = models.CharField( max_length=100 )
    
    # address data
    street = models.CharField( max_length=50 )
    zip_code = models.CharField( max_length=5 )
    city = models.CharField( max_length=50 )
    
    annotation = models.CharField( max_length=500 )
    
    # location data
    lat = models.FloatField()
    lon = models.FloatField()
    
    # verification
    verified = models.BooleanField()
    verification_date = models.DateField()
    
    filters = models.ManyToManyField( POIFilter )
    seals = models.ManyToManyField( Seal )
    
    def __str__( self ):
        return '%s - (%s)' % (self.name, self.city)
