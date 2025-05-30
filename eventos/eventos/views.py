from .models import Evento
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_historia(data):
    r = requests.get(settings.PATH_HIS, headers={"Accept":"application/json"})
    historias = r.json()
    for historia in historias:
        if data["historiaPaciente"] == historia["id"]:
            return True
    return False

def check_rol():
    r = requests.get(settings.PATH_LOG, headers={"Accept":"application/json"})
    if r.status_code == 404:
        return False
    elif len(r.json()) != 0:
        usuario = r.json()
        if usuario["rol"] in ["medico", "medica", "enfermera", "enfermero"]:
            return True
        else:
            return False
def EventoList(request):
    if check_rol():
        queryset = Evento.objects.all()
        context = list(queryset.values('id', 'fecha', 'historiaPaciente', 'especialidad', 'comentarios'))
        return JsonResponse(context, safe=False)
    return HttpResponse("Usuario actual no autorizado y/o no ingresado", status=403)

def EventoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_historia(data_json):
            evento = Evento()
            evento.fecha = data_json['fecha']
            evento.historiaPaciente = data_json['historiaPaciente']
            evento.especialidad = data_json['especialidad']
            evento.comentarios = data_json['comentarios']
            evento.save()
            return HttpResponse("Evento registrado exitosamente")
        else:
            return HttpResponse("Evento no registrado. Paciente o historia clínica no existente")

def EventosCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        evento_list = []
        for evento in data_json:
                    if check_historia(evento) == True:
                        dbevento = Evento()
                        dbevento.fecha = evento['fecha']
                        dbevento.historiaPaciente = evento['historiaPaciente']
                        dbevento.especialidad = evento['especialidad']
                        dbevento.comentarios = evento['comentarios']
                        evento_list.append(dbevento)
                    else:
                        return HttpResponse("Evento no registrado. Paciente o historia clínica no existente")
        
        Evento.objects.bulk_create(evento_list)
        return HttpResponse("Eventos Médicos cargados exitosamente") 
