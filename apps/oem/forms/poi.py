#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from django.forms.widgets import Textarea

from apps.oem.models.poi import POI


class AddPOIForm( ModelForm ):
    class Meta:
        model = POI
        fields = ('name', 'street', 'city', 'zip_code', 'text', 'filters', 'seals')
        labels = {
            'street' : 'Straẞe',
            'city' : 'Stadt',
            'zip_code' : 'PLZ',
            'text' : 'Beschreibung',
            'filters' : 'Filter',
            'seals' : 'Siegel',
        }
        widgets = {
            'text' : Textarea(attrs = {'cols':'40', 'rows':'5'}),
            'filters' : CheckboxSelectMultiple(),
        }


class EditPOIForm( ModelForm ):
    class Meta:
        model = POI
        exclude = ('verified', 'verification_date')