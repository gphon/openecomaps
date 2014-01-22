#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from apps.oem.models.area import Area
from apps.oem.models.flyer_page import FlyerPage
from apps.oem.models.oem_user import OEMUser
from apps.oem.models.poi import POI
from apps.oem.models.poi_filter import POIFilter
from apps.oem.models.seal_page import SealPage

import datetime
import os
from apps.oem.models.category import Category


DATA_FILE = './data.json'


def htmlspecialchars( text ):
    return text.replace('ä', '&auml;').replace('Ä', '&Auml;'). \
                replace('ö', '&ouml;').replace('Ö', '&Ouml;'). \
                replace('ü', '&uuml;').replace('Ü', '&Uuml;'). \
                replace('%', '%%').replace('ß', '&szlig;')


def delete():
    users = OEMUser.objects.exclude( is_staff=True )
    users.delete()
    
    areas = Area.objects.all()
    areas.delete()
    
    pages = FlyerPage.objects.all()
    pages.delete()
    
    pois = POI.objects.all()
    pois.delete()
    
    seals = SealPage.objects.all()
    seals.delete()


def create_dummy_data( request ):
    delete()
    
    f = open( os.path.join( os.path.dirname( __file__ ), DATA_FILE ), 'r' )
    data = eval( f.read() )
    f.close()
    
    for item in data['users']:
        user = OEMUser.objects.create_user( username = item['username'],
                                            password = item['password'],
                                            email = item['email'],
                                            group_name = item['group_name'] )
        user.save()
    #end for
    
    ###########################################################################
    
    for item in data['areas']:
        area = Area( name=item['name'],
                     lat_top  = item['lat_top'],    lat_bottom = item['lat_bottom'],
                     lon_left = item['lon_left'],   lon_right  = item['lon_right'] )
        area.save()
        
        for name in item['user']:
            group = get_object_or_404( OEMUser, username=name )
            group.areas.add( area )
        #end for
    #end for
    
    ###########################################################################
    
    for item in data['seals']:
        seal_page = SealPage(   name = item['name'],
                                text = htmlspecialchars( item['text'] ),
                                image = item['image'] )
        seal_page.save()
        
        for name in item['filters']:
            poi_filter = get_object_or_404( POIFilter, name__iexact=name )
            seal_page.filters.add( poi_filter )
        #end for
    #end for
    
    ###########################################################################
    
    for item in data['pois']:
        poi = POI(  name = item['name'],
                    street = item['street'],
                    zip_code = item['zip_code'],
                    city = item['city'],
                    text = item['text'],
                    lat = item['lat'],
                    lon = item['lon'],
                    verified = item['verified'],
                    verification_date = datetime.datetime.strptime( item['verification_date'], '%d.%m.%Y' ) )
        poi.save()
        
        for name in item['filters']:
            poi_filter = get_object_or_404( POIFilter, name__iexact=name )
            poi.filters.add( poi_filter )
        #end for
        
        for name in item['seals']:
            seal = get_object_or_404( SealPage, name__iexact=name )
            poi.seals.add( seal )
        #end for
    #end for
    
    ###########################################################################
    
    for item in data['pages']:
        page = FlyerPage( title = item['title'],
                          text = item['text'],
                          image = item['image'],
                          flyer = item['flyer'],
                          modified = datetime.datetime.strptime( item['modified'], '%d.%m.%Y %H:%M' ),
                          user = get_object_or_404( OEMUser, username__iexact=item['user'] ),
                          category = get_object_or_404( Category, name__iexact=item['category'] ) )
        page.save()
    #end for
    
    return HttpResponse('success')