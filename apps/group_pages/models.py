from django.db import models

from apps.auth.models import GPGroup


class PageCategory( models.Model ):
    name = models.CharField( max_length=50 )
    
    groups = models.ManyToManyField( GPGroup )
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Page( models.Model ):
    title = models.CharField( max_length=50 )
    text = models.TextField()
    image = models.ImageField(upload_to='/user_content/img')
    flyer = models.FileField(upload_to='/user_content/bin')
    modified = models.DateTimeField()
    
    group = models.ForeignKey( GPGroup )
    page_category = models.ForeignKey( PageCategory )
    
    def __str__(self):
        return self.title