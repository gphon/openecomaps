#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.db import models
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.widgets import Textarea

from apps.map.models.poi_filter import POIFilter
from apps.pages.models.seal_page import SealPage

import datetime


class POI( models.Model ):
    name = models.CharField( max_length=100 )
    
    # address data
    street = models.CharField( max_length=50 )
    zip_code = models.CharField( max_length=5 )
    city = models.CharField( max_length=50 )
    
    text = models.CharField( max_length=500, blank=True )
    
    # location data
    lat = models.FloatField()
    lon = models.FloatField()
    
    # verification
    verified = models.BooleanField( default=False )
    verification_date = models.DateField( default=datetime.date.today() )
    
    filters = models.ManyToManyField( POIFilter )
    seals = models.ManyToManyField( SealPage, blank=True )
    
    def __str__( self ):
        return '%s - (%s)' % (self.name, self.city)
    
    class Meta:
        app_label = 'map'


class POIForm( ModelForm ):
    class Meta:
        model = POI
        exclude = ('verified', 'verification_date')


class AddPOIForm( ModelForm ):
    class Meta:
        model = POI
        fields = ('name', 'street', 'city', 'zip_code', 'text', 'filters', 'seals')
        labels = {
            'street' : 'Strasse',
            'city' : 'Stadt',
            'zip_code' : 'PLZ',
            'text' : 'Beschreibung',
            'seals' : 'Siegel',
        }
        widgets = {
            'text' : Textarea(attrs = {'cols':'40', 'rows':'5'}),
            'filters' : CheckboxSelectMultiple(),
        }