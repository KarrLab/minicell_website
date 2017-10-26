""" HTML GUI URL patterns
:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-10-25
:Copyright: 2017, Karr Lab
:License: MIT
"""

from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',                views.index,        name='index'),
    url(r'^research/*$',      views.research,     name='research'),
    url(r'^education/*$',     views.education,    name='education'),
    url(r'^resources/*$',     views.resources,    name='resources'),
    url(r'^events/*$',        views.events,       name='events'),
    url(r'^publications/*$',  views.publications, name='publications'),
    url(r'^people/*$',        views.people,       name='people'),
    url(r'^contact/*$',       views.contact,      name='contact'),

    url(r'^login/*$',         views.login,        name='login'),
    url(r'^logout/*$',        views.logout,       name='logout'),

    url(r'^sitemap.xml$',     views.sitemap,      name='sitemap'),
    url(r'^robots.txt$',      views.robots,       name='robots'),
]
