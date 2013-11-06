from django.db import models
from django.forms import ModelForm

from apps.auth.models.gp_group import GPGroup
from apps.pages.models.category import Category


def upload_image_handler( instance, filename ):
    filepath = filename
    print(filepath)
    return filepath


class FlyerPage( models.Model ):
    title = models.CharField( max_length=50 )
    text = models.TextField()
    image = models.ImageField(upload_to=upload_image_handler)
    flyer = models.FileField(upload_to='/user_content/bin')
    modified = models.DateTimeField()
    
    group = models.ForeignKey( GPGroup )
    category = models.ForeignKey( Category )
    
    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'pages'


class FlyerPageForm( ModelForm ):
    class Meta:
        model = FlyerPage
        fields = ('title', 'text', 'image', 'flyer')