from django.db import models

from apps.oem.models.poi_filter import POIFilter


class SealPage( models.Model ):
    name = models.CharField( max_length=40 )
    text = models.TextField()
    image = models.ImageField( upload_to='/img/seals')
    
    filters = models.ManyToManyField( POIFilter )
    
    def get_text( self ):
        return self.text
    
    def print_thumbnail( self ):
        return '<img src="%s" width="150">' % self.image.url
    
    def __str__( self ):
        return self.name
    
    class Meta:
        app_label = 'oem'