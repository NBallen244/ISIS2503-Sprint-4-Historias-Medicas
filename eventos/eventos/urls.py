from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^eventos/', views.MeasurementList),
    url(r'^eventocreate/$', csrf_exempt(views.MeasurementCreate), name='eventoCreate'),
    url(r'^createeventos/$', csrf_exempt(views.MeasurementsCreate), name='createEventos'),
]