#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.contrib.auth.models import User
from django.http import HttpResponse

from apps.auth.models import GPGroup
from apps.dummy_data.dummy_data import *
from apps.map.models import Area
from apps.map.models import POI
from apps.map.models import POIFilter
from apps.pages.models import Category
from apps.pages.models import FlyerPage
from apps.pages.models import SealPage

import datetime


def convert2html( text ):
    return text.replace('ä', '&auml;').replace('Ä', '&Auml;'). \
                replace('ö', '&ouml;').replace('Ö', '&Ouml;'). \
                replace('ü', '&uuml;').replace('Ü', '&Uuml;'). \
                replace('%', '%%').replace('ß', '&szlig;')


def delete_data_in_db():
    groups = GPGroup.objects.all()
    groups.delete()
    areas = Area.objects.all()
    areas.delete()
    pages = FlyerPage.objects.all()
    pages.delete()
    categories = Category.objects.all()
    categories.delete()
    pois = POI.objects.all()
    pois.delete()
    poi_filters = POIFilter.objects.all()
    poi_filters.delete()
    seals = SealPage.objects.all()
    seals.delete()


def create_dummy_data( request ):
    delete_data_in_db()
    
    try:
        user_potsdam = User.objects.get( username='potsdam' )
    except:
        user_potsdam = User.objects.create_user( username='potsdam',
                                             email = 'a@b.de', password='123' )
    user_potsdam.save()
    
    try:
        user_berlin = User.objects.get( username='berlin' )
    except:
        user_berlin = User.objects.create_user( username='berlin',
                                             email = 'a@b.de', password='123' )
    user_berlin.save()
    
    try:
        user_stuttgart = User.objects.get( username='stuttgart' )
    except:
        user_stuttgart = User.objects.create_user( username='stuttgart',
                                             email = 'a@b.de', password='123' )
    user_stuttgart.save()
    
    try:
        user_hamburg = User.objects.get( username='hamburg' )
    except:
        user_hamburg = User.objects.create_user( username='hamburg',
                                             email = 'a@b.de', password='123' )
    user_hamburg.save()
    
    try:
        user_halle = User.objects.get( username='halle' )
    except:
        user_halle = User.objects.create_user( username='halle',
                                             email = 'a@b.de', password='123' )
    user_halle.save()
    
    try:
        user_cottbus = User.objects.get( username='cottbus' )
    except:
        user_cottbus = User.objects.create_user( username='cottbus',
                                             email = 'a@b.de', password='123' )
    user_halle.save()
    
    ###########################################################################
    
    area_potsdam = Area(
                name = 'Potsdam',
                lat_top  = 52.512878,   lat_bottom = 52.342996,
                lon_left = 12.885879,   lon_right  = 13.167087 )
    area_potsdam.save()
    
    area_stuttgart = Area(
                name = 'Stuttgart',
                lat_top  = 48.865166,   lat_bottom = 48.692773,
                lon_left =  9.036201,   lon_right  =  9.315666 )
    area_stuttgart.save()
    
    area_werder = Area(
                name = 'Werder (Havel)',
                lat_top  = 52.460403,   lat_bottom = 52.299242,
                lon_left = 12.801449,   lon_right  = 12.96141 )
    area_werder.save(),
    
    ###########################################################################
    
    group_b = GPGroup( name = 'Berlin',     user = user_berlin )
    group_b.save()
    
    group_p = GPGroup( name = 'Potsdam',    user = user_potsdam )
    group_p.save()
    
    group_s = GPGroup( name = 'Stuttgart',  user = user_stuttgart )
    group_s.save()
    
    group_hh = GPGroup( name = 'Hamburg',   user = user_hamburg )
    group_hh.save()
    
    group_halle = GPGroup( name = 'Halle',  user = user_halle )
    group_halle.save()
    
    # assign areas to groups
    group_p.areas.add( area_potsdam, area_werder )
    group_s.areas.add( area_stuttgart )
    
    ###########################################################################
    
    c_fish = Category( name = 'Fisch' )
    c_fish.save()
    
    c_textiles = Category( name = 'Textilien' )
    c_textiles.save()
    
    c_paper = Category( name = 'Papier' )
    c_paper.save()
    
    c_misc = Category( name = 'sonstiges' )
    c_misc.save()
    
    c_gmo = Category( name = 'Gentechnik' )
    c_gmo.save()
    
    ###########################################################################
    
    filter_lebensmittel = POIFilter( name = 'Lebensmittel', colour = '#00ff00' )
    filter_lebensmittel.save()
    
    filter_textilien = POIFilter( name = 'Textilien', colour = '#0000ff' )
    filter_textilien.save()
    
    filter_papier = POIFilter( name = 'Papier / Holz', colour = '#ff0000' )
    filter_papier.save()
    
    filter_kosmetik = POIFilter( name = 'Kosmetik', colour = '#ffff00' )
    filter_kosmetik.save()
    
    filter_mobilitaet = POIFilter( name = 'Mobilitaet', colour = '#ff00ff' )
    filter_mobilitaet.save()
    
    filter_sonstiges = POIFilter( name = 'sonstiges', colour = '#00ffff' )
    filter_sonstiges.save()
    
    ###########################################################################
    
    
    seal_demeter = SealPage( name = SEAL_DEMETER_NAME,
                             text = convert2html( SEAL_DEMETER_DESCRIPTION ),
                             image = SEAL_DEMETER_IMAGE )
    seal_demeter.save()
    
    seal_eu_bio = SealPage( name = SEAL_EU_BIO_NAME,
                            text = convert2html( SEAL_EU_BIO_DESCRIPTION ),
                            image = SEAL_EU_BIO_IMAGE )
    seal_eu_bio.save()
    
    seal_fsc = SealPage( name = SEAL_FSC_NAME,
                         text = convert2html( SEAL_FSC_DESCRIPTION ),
                         image = SEAL_FSC_IMAGE )
    seal_fsc.save()
    
    seal_ft = SealPage( name = SEAL_FAIRTRADE_NAME,
                        text = convert2html( SEAL_FAIRTRADE_DESCRIPTION ),
                        image = SEAL_FAIRTRADE_IMAGE )
    seal_ft.save()
    
    seal_msc = SealPage( name = SEAL_MSC_NAME,
                         text = convert2html( SEAL_MSC_DESCRIPTION ),
                         image = SEAL_MSC_IMAGE )
    seal_msc.save()
    
    seal_demeter.filters.add( filter_lebensmittel )
    seal_eu_bio.filters.add( filter_lebensmittel )
    seal_fsc.filters.add( filter_papier )
    seal_ft.filters.add( filter_kosmetik, filter_lebensmittel, filter_sonstiges )
    seal_msc.filters.add( filter_lebensmittel )
    
    ###########################################################################
    
    poi1 = POI( name = 'Cafe Kieselstein',
                street = 'Hegelallee 23',
                zip_code = '14467',             city = 'Potsdam',
                text = 'toller laden',
                lat = 52.402123,                lon = 13.048488,
                verified = False,
                verification_date = datetime.date.fromtimestamp(0) )
    poi1.save()
    
    poi2 = POI( name = 'Schalotte Naturkost',
                street = 'Charlottenstrasse 30',
                zip_code = '14467',             city = 'Potsdam',
                text = 'Bioladen',
                lat = 52.399372,                lon = 13.055376,
                verified = True,
                verification_date = datetime.date.today() )
    poi2.save()
    
    poi3 = POI( name = 'Vitalia Reformhaus GmbH',
                street = 'Rotebuehlstrasse 59',
                zip_code = '70178',             city = 'Stuttgart',
                text = 'Reformhaus',
                lat = 48.773077,                lon = 9.16796,
                verified = False,
                verification_date = datetime.date.fromtimestamp(0) )
    poi3.save()
    
    poi4 = POI( name = 'BioStube / Michael Chilla-Jung',
                street = 'Mielestrasse 2',
                zip_code = '14542',             city = 'Werder (Havel)',
                text = 'kenn ich nich',
                lat = 52.403885,                lon = 12.910467,
                verified = False,
                verification_date = datetime.date.fromtimestamp(0) )
    poi4.save()
    
    # assign pois to categories
    poi1.filters.add( filter_lebensmittel )
    poi2.filters.add( filter_lebensmittel, filter_papier )
    poi3.filters.add( filter_lebensmittel )
    poi4.filters.add( filter_papier )
    
    # assign pois to seals
    poi1.seals.add( seal_demeter )
    poi2.seals.add( seal_demeter, seal_ft )
    poi3.seals.add( seal_ft )
    poi4.seals.add( seal_demeter )
    
    ###########################################################################
    
    page1 = FlyerPage(  title = PAGE_FISH_S_TITLE,      text = convert2html( PAGE_FISH_S_TEXT ),
                        image = PAGE_FISH_S_IMAGE,      flyer = PAGE_FISH_S_FLYER,
                        modified = datetime.datetime.now(),
                        group = group_s,
                        category = c_fish )
    page1.save()
    
    page2 = FlyerPage(  title = PAGE_PAPER_B_TITLE,     text = convert2html( PAGE_PAPER_B_TEXT ),
                        image = PAGE_PAPER_B_IMAGE,     flyer = PAGE_PAPER_B_FLYER,
                        modified = datetime.datetime.now(),
                        group = group_b,
                        category = c_paper )
    page2.save()
    
    page3 = FlyerPage(  title = PAGE_PAPER_P_TITLE,     text = convert2html( PAGE_PAPER_P_TEXT ),
                        image = PAGE_PAPER_P_IMAGE,     flyer = PAGE_PAPER_P_FLYER,
                        modified = datetime.datetime.now(),
                        group = group_p,
                        category = c_paper )
    page3.save()
    
    page4 = FlyerPage(  title = PAGE_PAPER_Halle_TITLE, text = convert2html( PAGE_PAPER_Halle_TEXT ),
                        image = PAGE_PAPER_Halle_IMAGE, flyer = PAGE_PAPER_Halle_FLYER,
                        modified = datetime.datetime.now(),
                        group = group_halle,
                        category = c_paper )
    page4.save()
    
    page5 = FlyerPage(  title = PAGE_PAPER_HH_TITLE,    text = convert2html( PAGE_PAPER_HH_TEXT ),
                        image = PAGE_PAPER_HH_IMAGE,    flyer = PAGE_PAPER_HH_FLYER,
                        modified = datetime.datetime.now(),
                        group = group_hh,
                        category = c_paper )
    page5.save()
    
    page6 = FlyerPage(  title = PAGE_FISH_P_TITLE,      text = convert2html( PAGE_FISH_P_TEXT ),
                        image = PAGE_FISH_P_IMAGE,      flyer = PAGE_FISH_P_FLYER,
                        modified = datetime.datetime.now(),
                        group = group_p,
                        category = c_fish )
    page6.save()
    
    return HttpResponse('success')




def show_dummy_data( request ):
    output = """
    <b>fetch all greenpeace groups:</b><br>
    for group in GPGroup.objects.all():<br>
    ........print group<br><br>
    
    <table border="1">
        <tr><td>name</td><td>user</td></tr>"""
    for group in GPGroup.objects.all():
        output += '<tr>'
        output += '<td>%s</td>' % group.name
        output += '<td>%s</td>' % group.user
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
    for poi_filter in POIFilter.objects.all():
        output += '>>> <font color="%s">%s</font><br>' % ( poi_filter.colour,
                                                            poi_filter.name )
    
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
        if 'Ernaehrung' in [poi_filter.name for poi_filter in poi.filters.all()]:
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