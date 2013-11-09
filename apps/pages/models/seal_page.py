from django.db import models

from apps.map.models.poi_filter import POIFilter


class SealPage( models.Model ):
    name = models.CharField( max_length=40 )
    text = models.CharField( max_length=500 )
    image = models.ImageField( upload_to='user_content/img/seals')
    
    filters = models.ManyToManyField( POIFilter )
    
    def __str__( self ):
        return self.name
    
    class Meta:
        app_label = 'pages'