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

###############################################################################

class GPGroup( models.Model ):
    name     = models.CharField( max_length=100 )
    password = models.CharField( max_length=32 )  # stored as md5 hashdigest
    email    = models.EmailField()
    
    areas = models.ManyToManyField( Area )
    
    def __str__( self ):
        return self.name

###############################################################################

class POICategory( models.Model ):
    name = models.CharField( max_length=40 )
    colour = models.CharField( max_length=7 )
    
    def __str__( self ):
        return self.name

###############################################################################

class Seal( models.Model ):
    name = models.CharField( max_length=40 )
    annotation = models.CharField( max_length=500 )
    image = models.URLField()
    
    def __str__( self ):
        return self.name

###############################################################################

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
    
    categories = models.ManyToManyField( POICategory )
    seals = models.ManyToManyField( Seal )
    
    def __str__( self ):
        return '%s - (%s)' % (self.name, self.city)

