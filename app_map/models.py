from django.db import models


class City( models.Model ):
    name = models.CharField(max_length=20)
    coord_lon = models.FloatField()
    coord_lat = models.FloatField()
    coord_zoom = models.IntegerField()

    def __eq__(self, other):
        return self.id == other.id
    
    def __str__(self):
        return '%s (%s/%s) - %s' % (self.name, self.coord_lon, self.coord_lat, self.coord_zoom)



class Store( models.Model ):
    name = models.CharField( max_length=100 )
    
    # address data
    street = models.CharField( max_length=50 )
    city = models.CharField( max_length=50 )
    zip_code = models.CharField( max_length=5)
