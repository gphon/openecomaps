from django.db import models

#from apps.auth.models.gp_group import GPGroup


class Category( models.Model ):
    name = models.CharField( max_length=50 )
    
    #groups = models.ManyToManyField( GPGroup )
    
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'group_pages'
        ordering = ['name']