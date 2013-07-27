from django.shortcuts import render_to_response



def info_view(request, template_name):
    return render_to_response( template_name )
