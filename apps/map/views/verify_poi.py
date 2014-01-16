from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from apps.map.models.poi import POI

import datetime


@login_required( login_url="/login" )
def verify_poi( request, poi_id ):
    poi = get_object_or_404( POI, id=poi_id )
    #TODO: check if access is allowed
    if poi.verified:
        poi.verified = False
    else:
        poi.verified = True
        poi.verification_date = datetime.date.today()
    poi.save()
    return HttpResponseRedirect( '/overview/poi' )