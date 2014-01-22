from django.forms import ModelForm

from apps.oem.models.flyer_page import FlyerPage


class FlyerPageForm( ModelForm ):
    class Meta:
        model = FlyerPage
        fields = ('title', 'text', 'image', 'flyer')