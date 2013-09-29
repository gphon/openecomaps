from django.http import HttpResponse
from django.test import TestCase

from app_oem.models import Area
from app_oem.models import GPGroup
from app_oem.models import POI
from app_oem.models import POICategory
from app_oem.models import Seal

import datetime
import hashlib




def create_dummy_data_view( request ):
    
    a1 = Area(  name = 'Potsdam',
                lat_top  = 52.512878,   lat_bottom = 52.342996,
                lon_left = 12.885879,   lon_right  = 13.167087 )
    a1.save()
    
    a2 = Area(  name = 'Stuttgart',
                lat_top  = 48.865166,   lat_bottom = 48.692773,
                lon_left =  9.036201,   lon_right  =  9.315666 )
    a2.save()
    
    a3 = Area(  name = 'Werder (Havel)',
                lat_top  = 52.460403,   lat_bottom = 52.299242,
                lon_left = 12.801449,   lon_right  = 12.96141 )
    a3.save(),
    
    ###########################################################################
    
    g1 = GPGroup(   name = 'Duesseldorf',
                    password = hashlib.md5(b'321').hexdigest(),
                    email = 'info@duesseldorf.greenpeace.de' )
    g1.save()
    
    g2 = GPGroup(   name = 'Potsdam',
                    password = hashlib.md5(b'123').hexdigest(),
                    email = 'info@potsdam.greenpeace.de' )
    g2.save()
    
    g3 = GPGroup(   name = 'Stuttgart',
                    password = hashlib.md5(b'abc').hexdigest(),
                    email = 'info@stuttgart.greenpeace.de' )
    g3.save()
    
    # assign areas to groups
    g2.areas.add( a1, a3 )
    g3.areas.add( a2 )
    
    ###########################################################################
    
    c1 = POICategory(   name = 'Ernaehrung',
                        colour = '#00ff00' )
    c1.save()
    
    c2 = POICategory(   name = 'Textilien',
                        colour = '#0000ff' )
    c2.save()
    
    ###########################################################################
    
    s1 = Seal(  name = 'Fair Trade',
                annotation = 'Siegel fuer fairen Handel',
                image = 'fairtrade.svg' )
    s1.save()
    
    s2 = Seal(  name = 'FSC',
                annotation = 'forest stewardship council',
                image = 'fsc.svg' )
    s2.save()
    
    s3 = Seal(  name = 'Demeter',
                annotation = 'tollstes Biosiegel ueberhaupt',
                image = 'demeter.svg' )
    s3.save()
    
    ###########################################################################
    
    p1 = POI(   name = 'Cafe Kieselstein',
                street = 'Hegelallee 23',
                zip_code = '14467',
                city = 'Potsdam',
                annotation = 'toller laden',
                lat = 52.402123,
                lon = 13.048488,
                verified = False,
                verification_date = datetime.date.fromtimestamp(0) )
    p1.save()
    
    p2 = POI(   name = 'Schalotte Naturkost',
                street = 'Charlottenstrasse 30',
                zip_code = '14467',
                city = 'Potsdam',
                annotation = 'Bioladen',
                lat = 52.399372,
                lon = 13.055376,
                verified = True,
                verification_date = datetime.date.today() )
    p2.save()
    
    p3 = POI(   name = 'Vitalia Reformhaus GmbH',
                street = 'Rotebuehlstrasse 59',
                zip_code = '70178',
                city = 'Stuttgart',
                annotation = 'Reformhaus',
                lat = 48.773077,
                lon = 9.16796,
                verified = False,
                verification_date = datetime.date.fromtimestamp(0) )
    p3.save()
    
    p4 = POI(   name = 'BioStube / Michael Chilla-Jung',
                street = 'Mielestrasse 2',
                zip_code = '14542',
                city = 'Werder (Havel)',
                annotation = 'kenn ich nich',
                lat = 52.403885,
                lon = 12.910467,
                verified = False,
                verification_date = datetime.date.fromtimestamp(0) )
    p4.save()
    
    # assign pois to categories
    p1.categories.add( c1 )
    p2.categories.add( c1 )
    p3.categories.add( c1 )
    
    # assign pois to seals
    p1.seals.add( s1 )
    p2.seals.add( s1, s3 )
    p3.seals.add( s3 )
    
    return HttpResponse('success')





def show_dummy_data_view( request ):
    output = """
    <b>fetch all greenpeace groups:</b><br>
    for group in GPGroup.objects.all():<br>
    ........print group<br><br>
    
    <table border="1">
        <tr><td>name</td><td>password</td><td>email</td></tr>"""
    for group in GPGroup.objects.all():
        output += '<tr>'
        output += '<td>%s</td>' % group.name
        output += '<td>%s</td>' % group.password
        output += '<td>%s</td>' % group.email
        output += '</tr>'
    output += '</table>'
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all areas:</b><br>
    for area in Area.objects.all():<br>
    ........print area<br><br>
    
    <table border="1">
        <tr><td>name</td><td>lat_top</td><td>lat_bottom</td><td>lon_left</td><td>lon_right</td></tr>"""
    for area in Area.objects.all():
        output += '<tr>'
        output += '<td>%s</td>' % area.name
        output += '<td>%s</td>' % area.lat_top
        output += '<td>%s</td>' % area.lat_bottom
        output += '<td>%s</td>' % area.lon_left
        output += '<td>%s</td>' % area.lon_right
        output += '</tr>'
    output += '</table>'
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all areas related to greenpeace potsdam:</b><br>
    potsdam = GPGroup.objects.get(name='Potsdam')<br>
    for area in potsdam.areas.all():<br>
    ........print area<br><br>"""
    potsdam = GPGroup.objects.get(name='Potsdam')
    for area in potsdam.areas.all():
        output += '>>> %s<br>' % area.name
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all POI categories:</b><br>
    for category in POICategory.objects.all():<br>
    ........print category<br><br>"""
    for category in POICategory.objects.all():
        output += '>>> <font color="%s">%s</font><br>' % (category.colour, category.name)
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all seals:</b><br>
    for seal in Seal.objects.all():<br>
    ........print Seal<br><br>
    
    <table border="1">
        <tr><td>name</td><td>annotation</td><td>image</td></tr>"""
    for seal in Seal.objects.all():
        output += '<tr>'
        output += '<td>%s</td>' % seal.name
        output += '<td>%s</td>' % seal.annotation
        output += '<td><img src="static/img/test/%s" width="50"></td>' % seal.image
        output += '</tr>'
    output += '</table>'

    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all pois:</b><br>
    for poi in POI.objects.all():<br>
    ........print poi<br><br>
    
    <table border="1">
        <tr><td>name</td><td>street</td><td>zip_code</td><td>city</td><td>annotation</td><td>lat</td><td>lon</td><td>verified</td><td>verification_date</td></tr>"""
    for poi in POI.objects.all():
        output += '<tr>'
        output += '<td>%s</td>' % poi.name
        output += '<td>%s</td>' % poi.street
        output += '<td>%s</td>' % poi.zip_code
        output += '<td>%s</td>' % poi.city
        output += '<td>%s</td>' % poi.annotation
        output += '<td>%s</td>' % poi.lat
        output += '<td>%s</td>' % poi.lon
        output += '<td>%s</td>' % poi.verified
        output += '<td>%s</td>' % poi.verification_date
        output += '</tr>'
    output += '</table>'
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all poi's related to greenpeace potsdam:</b><br>
    potsdam = GPGroup.objects.get( name='Potsdam' )<br>
    areas = potsdam.areas.all()<br>
    for poi in POI.objects.all():<br>
    ........if True in [ area.lat_bottom <= poi.lat <= area.lat_top<br>
    ................................and area.lon_left <= poi.lon <= area.lon_right<br>
    ................................for area in areas ]:<br>
    ................print poi<br><br>"""
    
    potsdam = GPGroup.objects.get( name='Potsdam' )
    areas = potsdam.areas.all()
    for poi in POI.objects.all():
        if True in [ area.lat_bottom <= poi.lat <= area.lat_top
                                and area.lon_left <= poi.lon <= area.lon_right
                                for area in areas ]:
            output += '>>> %s<br>' % poi.name
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all poi's in category ernaehrung:</b><br>
    for poi in POI.objects.all():<br>
    ........if 'Ernaehrung' in [category.name for category in poi.categories.all()]:<br>
    ................print poi<br><br>"""
    
    for poi in POI.objects.all():
        if 'Ernaehrung' in [category.name for category in poi.categories.all()]:
            output += '>>> %s<br>' % poi.name
    
    ###########################################################################
    
    output += """<hr><br>
    <b>fetch all poi's with demeter seal:</b><br>
    for poi in POI.objects.all():<br>
    ........if 'Ernaehrung' in [category.name for category in poi.categories.all()]:<br>
    ................print poi<br><br>"""
    
    for poi in POI.objects.all():
        if 'Demeter' in [seal.name for seal in poi.seals.all()]:
            output += '>>> %s<br>' % poi.name

    return HttpResponse( output )
