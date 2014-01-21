#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from apps.auth.models.oem_user import OEMUser
from apps.map.models.area import Area
from apps.map.models.poi import POI
from apps.map.models.poi_filter import POIFilter
from apps.pages.models.category import Category
from apps.pages.models.flyer_page import FlyerPage
from apps.pages.models.seal_page import SealPage


def convert2html( text ):
    return text.replace('ä', '&auml;').replace('Ä', '&Auml;'). \
                replace('ö', '&ouml;').replace('Ö', '&Ouml;'). \
                replace('ü', '&uuml;').replace('Ü', '&Uuml;'). \
                replace('%', '%%').replace('ß', '&szlig;')


def delete_data_in_db():
    users = OEMUser.objects.all()
    users.delete()
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
    """
    try:
        user_potsdam = get_object_or_404( OEMUser, username='potsdam' )
    except:
        user_potsdam = OEMUser.objects.create_user( username='potsdam',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Potsdam' )
    user_potsdam.save()
    """
    
    ###########################################################################
    """
    area_potsdam = Area(    name = 'Potsdam',
                            lat_top  = 52.512878,   lat_bottom = 52.342996,
                            lon_left = 12.885879,   lon_right  = 13.167087 )
    area_potsdam.save()
    """
    
    ###########################################################################
    """
    c_fish = Category( name = 'Fisch' )
    c_fish.save()
    """
    
    ###########################################################################
    """
    filter_lebensmittel = POIFilter( name = 'Lebensmittel' )
    filter_lebensmittel.save()
    """
    
    ###########################################################################
    """
    seal_demeter = SealPage( name = SEAL_DEMETER_NAME,
                             text = convert2html( SEAL_DEMETER_DESCRIPTION ),
                             image = SEAL_DEMETER_IMAGE )
    seal_demeter.save()
    """
    
    ###########################################################################
    """
    poi1 = POI( name = POI1_NAME,
                street = convert2html( POI1_STREET ),
                zip_code = POI1_ZIP, city = POI1_CITY,
                text = POI1_TEXT,
                lat = POI1_LAT, lon = POI1_LON,
                verified = POI1_VERIFIED,
                verification_date = POI1_VERIFICATION_DATE )
    poi1.save()
    """
    
    ###########################################################################
    """
    page1 = FlyerPage(  title = PAGE_FISH_S_TITLE,      text = convert2html( PAGE_FISH_S_TEXT ),
                        image = PAGE_FISH_S_IMAGE,      flyer = PAGE_FISH_S_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_stuttgart,
                        category = c_fish )
    page1.save()
    """
    return HttpResponse('success')