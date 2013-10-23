from django.db import models

from apps.group_pages.models.seal import Seal
from apps.map.models.poi_filter import POIFilter


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
    
    class Meta:
        app_label = 'map'