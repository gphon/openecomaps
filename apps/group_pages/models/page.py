from django.db import models
from django.forms import ModelForm

from apps.auth.models.gp_group import GPGroup
from apps.group_pages.models.category import Category


class Page( models.Model ):
    title = models.CharField( max_length=50 )
    text = models.TextField()
    image = models.ImageField(upload_to='/user_content/img')
    flyer = models.FileField(upload_to='/user_content/bin')
    modified = models.DateTimeField()
    
    group = models.ForeignKey( GPGroup )
    category = models.ForeignKey( Category )
    
    def __str__(self):
        return self.title


class PageForm( ModelForm ):
    class Meta:
        model = Page
        fields = ('title', 'text', 'image', 'flyer')