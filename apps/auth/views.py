from django.core.context_processors import csrf
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import LoginForm




def overview( request ):
    if session.haskey( 'overview' ):
        latest_page = session['overview']
    else:
        latest_page = None
    return render_to_response( 'overview.html', context,
                                    context_instance=RequestContext(request) )


def login( request ):
    if request.method == 'POST':
        form = LoginForm( request.POST )
        if form.is_valid():
            groupname = form.cleaned_data['groupname'].lower()
            password = form.cleaned_data['password']
            
            user = auth.authenticate( username=groupname, password=password )
            if user is not None and user.is_active:
                auth.login( request, user )
                render_to_response( 'overview.html'
                                    context_instance=RequestContext(request) )
            #endif
        else:
            #TODO: error message
        #endif
    else:
        form = LoginForm()
    #endif
    
    context = {}
    context.update( csrf(request) )
    context['form'] = form
    return render_to_response( 'login.html', context,
                                    context_instance=RequestContext(request) )


def logout( request ):
    auth.logout( request )
    return render_to_response( 'home.html' )S
