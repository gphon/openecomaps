from django.db import models
from django.forms import ModelForm

from apps.pages.models.category import Category
from apps.auth.models.oem_user import OEMUser


class FlyerPage( models.Model ):
    title = models.CharField( max_length=50 )
    text = models.TextField()
    image = models.ImageField(upload_to='user_content/img/flyer')
    flyer = models.FileField(upload_to='user_content/bin')
    modified = models.DateTimeField()
    
    user = models.ForeignKey( OEMUser )
    category = models.ForeignKey( Category )
    
    def __str__(self):
        return self.title
    
    class Meta:
        app_label = 'pages'


class FlyerPageForm( ModelForm ):
    class Meta:
        model = FlyerPage
        fields = ('title', 'text', 'image', 'flyer')