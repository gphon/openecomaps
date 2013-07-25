from django.db import models


class Store( models.Model ):
    name = models.CharField( max_lenght=100 )
    
    # address data
    street = models.CharField( max_lenght=50 )
    city = models.CharField( max_lenght=50 )
    zip_code = models.CharField( max_lenght=5)
