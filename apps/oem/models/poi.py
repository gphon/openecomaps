from django.db import models

from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.seal_page import SealPage

import datetime


class POI( models.Model ):
    name = models.CharField( max_length=100 )
    
    # address data
    street = models.CharField( max_length=50 )
    zip_code = models.CharField( max_length=5 )
    city = models.CharField( max_length=50 )
    
    text = models.CharField( max_length=500, blank=True )
    
    opening_time = models.CharField( max_length=100, blank=True )
    website = models.URLField( blank=True )
    
    # location data
    lat = models.FloatField()
    lon = models.FloatField()
    
    # verification
    verified = models.BooleanField( default=False )
    verification_date = models.DateField( default=datetime.date.today() )
    
    filters = models.ManyToManyField( POIFilter )
    seals = models.ManyToManyField( SealPage, blank=True )
    
    def print_website_link( self ):
        return '<a href="%(url)s" target="_blank">%(url)s</a>' % {'url':self.website}
    website_link = property( print_website_link )
    
    def __str__( self ):
        return '%s - (%s)' % (self.name, self.city)
    
    class Meta:
        app_label = 'oem'