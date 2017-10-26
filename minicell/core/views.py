""" Core views
:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-10-26
:Copyright: 2017, Karr Lab
:License: MIT
"""

from datetime import datetime
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from minicell.site import settings
import os

###################
### pages
###################
def index(request):
    return render_template(request, 'index.html')
    
def research(request):
    return render_template(request, 'research.html')

def education(request):
    return render_template(request, 'education.html')

def resources(request):
    return render_template(request, 'resources.html')

def events(request):
    return render_template(request, 'events.html')
    
def publications(request):
    return render_template(request, 'publications.html')
    
def people(request):
    return render_template(request, 'people.html')

def contact(request):
    return render_template(request, 'contact.html')
    
@csrf_protect
@never_cache
def login(request):
    next = request.REQUEST.get('next', '')
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                  
            return HttpResponseRedirect(next)
    else:
        form = AuthenticationForm(request)

    request.session.set_test_cookie()
    return render_template(request, 'login.html', context={
        'form': form,
        'next': next,
        })
    
def logout(request):
    auth_logout(request)
    return render_template(request, 'logout.html')
    
###################
### sitemap, robots
###################
def sitemap(request):
    return render_template(request, 'sitemap.xml', context={'ROOT_URL': settings.ROOT_URL}, content_type='application/xml')
    
def robots(request):
    return render_template(request, 'robots.txt', context={'ROOT_DOMAIN': settings.ROOT_DOMAIN, 'ROOT_URL': settings.ROOT_URL}, content_type='plain/text')
    
###################
### helper functions
###################
def render_template(request, template, context=None, content_type='text/html'):
    ''' Returns rendered template
    Args:
        request (:obj:`django.http.request.HttpRequest`): HTTP request
        template (:obj:`str`): path to template to render_template
        context (:obj:`dict`, optional): dictionary of data needed to render template
        content_type (:obj:`str`, optional): mime type
    Returns:
        :obj:`django.http.HttpResponse`: HTTP response
    '''

    if context is None:
        context = {}

    #add data
    context['request'] = request
    context['last_updated_date'] = datetime.fromtimestamp(os.path.getmtime(os.path.join(settings.TEMPLATES[0]['DIRS'][0], template)))

    #render
    return render(request, template, context=context, content_type=content_type)
