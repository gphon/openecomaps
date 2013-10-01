#!/usr/bin/python
# -*- coding: latin-1 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def info( request, template_name ):
    template_path = 'info_pages/' + template_name + '.html'
    context = {
        'links' : [
            ('about', 'Über das Projekt'),
            ('copyright', 'Copyright'),
            ('impressum', 'Impressum'),
         ],
        'selected' : template_name,
    }
    return render_to_response( template_path, context,
                                    context_instance=RequestContext(request) )
