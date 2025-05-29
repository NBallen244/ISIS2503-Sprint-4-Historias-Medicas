from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^historias/', views.HistoriaList, name='historiaList'),
    url(r'^historiacreate/$', csrf_exempt(views.HistoriaCreate), name='historiaCreate'),
    url(r'^createhistorias/$', csrf_exempt(views.HistoriasCreate), name='createHistorias'),
]