from django.http import HttpResponse

from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.category import Category

import os


DATA_FILE = './dummy_data/data.json'


def init( request ):
    if len( Category.objects.all() ) and len( POIFilter.objects.all() ):
        return HttpResponse( 'already done' )
    
    f = open( os.path.join( os.path.dirname( __file__ ), DATA_FILE ), 'r' )
    data = eval( f.read() )
    f.close()
    
    for item in data['categories']:
        category = Category( name=item['name'] )
        category.save()
    #end for
    
    for item in data['filters']:
        poi_filter = POIFilter( name=item['name'] )
        poi_filter.save()
    #end for
    
    return HttpResponse( 'success' )