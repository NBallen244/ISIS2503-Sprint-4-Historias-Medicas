from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^eventos/', views.EventoList),
    url(r'^eventocreate/$', csrf_exempt(views.EventoCreate), name='eventoCreate'),
    url(r'^createeventos/$', csrf_exempt(views.EventosCreate), name='createEventos'),
]