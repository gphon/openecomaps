from django.db import models

from apps.oem.models.category import Category
from apps.oem.models.oem_user import OEMUser


class FlyerPage( models.Model ):
    title = models.CharField( max_length=50 )
    text = models.TextField()
    image = models.ImageField(upload_to='img')
    flyer = models.FileField(upload_to='bin')
    modified = models.DateTimeField()
    
    user = models.ForeignKey( OEMUser )
    category = models.ForeignKey( Category )
    
    def get_text( self ):
        text = self.text.replace( '\n', '<br>')
        text = text.replace( '[b]', '<b>' ).replace( '[/b]', '</b>' )
        text = text.replace( '[i]', '<i>' ).replace( '[/i]', '</i>' )
        text = text.replace( '[u]', '<u>' ).replace( '[/u]', '</u>' )
        return text
    
    def print_thumbnail( self ):
        return '''
            <a href="%(flyer_url)s">
                <img src="%(image_url)s" width="150">
            </a>
            <center>
                <a href="%(flyer_url)s">download</a>
            </center>
        ''' % { 'image_url':self.image.url, 'flyer_url':self.flyer.url }
    
    def __str__( self ):
        return self.title
    
    class Meta:
        app_label = 'oem'