#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from apps.auth.models.oem_user import OEMUser
from apps.dummy_data.dummy_data import *
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
    
    try:
        user_potsdam = get_object_or_404( OEMUser, username='potsdam' )
    except:
        user_potsdam = OEMUser.objects.create_user( username='potsdam',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Potsdam' )
    user_potsdam.save()
    
    try:
        user_berlin = get_object_or_404( OEMUser, username='berlin' )
    except:
        user_berlin = OEMUser.objects.create_user( username='berlin',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Berlin' )
    user_berlin.save()
    
    try:
        user_stuttgart = get_object_or_404( OEMUser, username='stuttgart' )
    except:
        user_stuttgart = OEMUser.objects.create_user( username='stuttgart',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Stuttgart' )
    user_stuttgart.save()
    
    try:
        user_hamburg = get_object_or_404( OEMUser, username='hamburg' )
    except:
        user_hamburg = OEMUser.objects.create_user( username='hamburg',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Hamburg' )
    user_hamburg.save()
    
    try:
        user_halle = get_object_or_404( OEMUser, username='halle' )
    except:
        user_halle = OEMUser.objects.create_user( username='halle',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Halle' )
    user_halle.save()
    
    try:
        user_cottbus = get_object_or_404( OEMUser, username='cottbus' )
    except:
        user_cottbus = OEMUser.objects.create_user( username='cottbus',
                                             email = 'a@b.de', password='123',
                                             group_name = 'Cottbus' )
    user_halle.save()
    
    ###########################################################################
    
    area_potsdam = Area(    name = 'Potsdam',
                            lat_top  = 52.512878,   lat_bottom = 52.342996,
                            lon_left = 12.885879,   lon_right  = 13.167087 )
    area_potsdam.save()
    
    area_stuttgart = Area(  name = 'Stuttgart',
                            lat_top  = 48.865166,   lat_bottom = 48.692773,
                            lon_left =  9.036201,   lon_right  =  9.315666 )
    area_stuttgart.save()
    
    area_werder = Area(     name = 'Werder (Havel)',
                            lat_top  = 52.460403,   lat_bottom = 52.299242,
                            lon_left = 12.801449,   lon_right  = 12.96141 )
    area_werder.save(),
    
    # assign areas to users
    user_potsdam.areas.add( area_potsdam, area_werder )
    user_stuttgart.areas.add( area_stuttgart )
    
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
    
    filter_papier = POIFilter( name = 'Papier_Holz', colour = '#ff0000' )
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
    
    poi1 = POI( name = POI1_NAME,
                street = convert2html( POI1_STREET ),
                zip_code = POI1_ZIP, city = POI1_CITY,
                text = POI1_TEXT,
                lat = POI1_LAT, lon = POI1_LON,
                verified = POI1_VERIFIED,
                verification_date = POI1_VERIFICATION_DATE )
    poi1.save()
    
    poi2 = POI( name = POI2_NAME,
                street = convert2html( POI2_STREET ),
                zip_code = POI2_ZIP, city = POI2_CITY,
                text = POI2_TEXT,
                lat = POI2_LAT, lon = POI2_LON,
                verified = POI2_VERIFIED,
                verification_date = POI2_VERIFICATION_DATE )
    poi2.save()
    
    poi3 = POI( name = POI3_NAME,
                street = convert2html( POI3_STREET ),
                zip_code = POI3_ZIP, city = POI3_CITY,
                text = POI3_TEXT,
                lat = POI3_LAT, lon = POI3_LON,
                verified = POI3_VERIFIED,
                verification_date = POI3_VERIFICATION_DATE )
    poi3.save()
    
    poi4 = POI( name = POI4_NAME,
                street = convert2html( POI4_STREET ),
                zip_code = POI4_ZIP, city = POI4_CITY,
                text = POI4_TEXT,
                lat = POI4_LAT, lon = POI4_LON,
                verified = POI4_VERIFIED,
                verification_date = POI4_VERIFICATION_DATE )
    poi4.save()
    
    poi5 = POI( name = POI5_NAME,
                street = convert2html( POI5_STREET ),
                zip_code = POI5_ZIP, city = POI5_CITY,
                text = POI5_TEXT,
                lat = POI5_LAT, lon = POI5_LON,
                verified = POI5_VERIFIED,
                verification_date = POI5_VERIFICATION_DATE )
    poi5.save()
    
    poi6 = POI( name = POI6_NAME,
                street = convert2html( POI6_STREET ),
                zip_code = POI6_ZIP, city = POI6_CITY,
                text = POI6_TEXT,
                lat = POI6_LAT, lon = POI6_LON,
                verified = POI6_VERIFIED,
                verification_date = POI6_VERIFICATION_DATE )
    poi6.save()
    
    poi7 = POI( name = POI7_NAME,
                street = convert2html( POI7_STREET ),
                zip_code = POI7_ZIP, city = POI7_CITY,
                text = POI7_TEXT,
                lat = POI7_LAT, lon = POI7_LON,
                verified = POI7_VERIFIED,
                verification_date = POI7_VERIFICATION_DATE )
    poi7.save()
    
    # assign pois to filters
    poi1.filters.add( filter_lebensmittel )
    poi2.filters.add( filter_lebensmittel )
    poi3.filters.add( filter_lebensmittel )
    poi4.filters.add( filter_lebensmittel )
    poi5.filters.add( filter_lebensmittel )
    poi6.filters.add( filter_lebensmittel, filter_textilien, filter_kosmetik )
    poi7.filters.add( filter_mobilitaet )
    
    # assign pois to seals
    poi1.seals.add( seal_demeter )
    poi2.seals.add( seal_demeter, seal_ft )
    poi3.seals.add( seal_ft )
    poi4.seals.add( seal_demeter )
    
    ###########################################################################
    
    page1 = FlyerPage(  title = PAGE_FISH_S_TITLE,      text = convert2html( PAGE_FISH_S_TEXT ),
                        image = PAGE_FISH_S_IMAGE,      flyer = PAGE_FISH_S_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_stuttgart,
                        category = c_fish )
    page1.save()
    
    page2 = FlyerPage(  title = PAGE_PAPER_B_TITLE,     text = convert2html( PAGE_PAPER_B_TEXT ),
                        image = PAGE_PAPER_B_IMAGE,     flyer = PAGE_PAPER_B_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_berlin,
                        category = c_paper )
    page2.save()
    
    page3 = FlyerPage(  title = PAGE_PAPER_P_TITLE,     text = convert2html( PAGE_PAPER_P_TEXT ),
                        image = PAGE_PAPER_P_IMAGE,     flyer = PAGE_PAPER_P_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_potsdam,
                        category = c_paper )
    page3.save()
    
    page4 = FlyerPage(  title = PAGE_PAPER_Halle_TITLE, text = convert2html( PAGE_PAPER_Halle_TEXT ),
                        image = PAGE_PAPER_Halle_IMAGE, flyer = PAGE_PAPER_Halle_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_halle,
                        category = c_paper )
    page4.save()
    
    page5 = FlyerPage(  title = PAGE_PAPER_HH_TITLE,    text = convert2html( PAGE_PAPER_HH_TEXT ),
                        image = PAGE_PAPER_HH_IMAGE,    flyer = PAGE_PAPER_HH_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_hamburg,
                        category = c_paper )
    page5.save()
    
    page6 = FlyerPage(  title = PAGE_FISH_P_TITLE,      text = convert2html( PAGE_FISH_P_TEXT ),
                        image = PAGE_FISH_P_IMAGE,      flyer = PAGE_FISH_P_FLYER,
                        modified = datetime.datetime.now(),
                        user = user_potsdam,
                        category = c_fish )
    page6.save()
    
    return HttpResponse('success')




def init( request ):
    for name in ['Fisch', 'Textilien', 'Papier / Holz', 'Gentechnik', 'sonstiges']:
        c = Category( name = name )
        c.save()
    #endfor
    
    ###########################################################################
    
    for name, colour in [ ('Lebensmittel','#00ff00'), ('Textilien','#0000ff'),
                          ('Papier_Holz','#ff0000'), ('Kosmetik','#ffff00'),
                          ('Mobilitaet','#ff00ff'), ('sonstiges','#00ffff') ]:
        f = POIFilter( name = name, colour = colour )
        f.save()
    
    return HttpResponse('success')