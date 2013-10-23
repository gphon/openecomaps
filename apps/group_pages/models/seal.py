from django.db import models


class Seal( models.Model ):
    name = models.CharField( max_length=40 )
    annotation = models.CharField( max_length=500 )
    image = models.URLField()
    
    def __str__( self ):
        return self.name
    
    class Meta:
        app_label = 'group_pages'