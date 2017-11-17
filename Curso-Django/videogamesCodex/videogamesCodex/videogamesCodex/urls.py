"""
Definition of urls for videogamesCodex.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^game\/(?P<id>[0-9]+)$', app.views.paginagame),
    url(r'^borrar\/(?P<id>[0-9]+)$', app.views.borrar_game),
    url(r'^crear\/{0,1}$', app.views.crear_game),
    url(r'^modificar\/(?P<id>[0-9]+)$', app.views.modificar_game),
    url(r'^ranking\/{0,1}$', app.views.ranking),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
