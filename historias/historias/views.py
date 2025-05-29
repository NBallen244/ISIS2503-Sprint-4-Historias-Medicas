from .models import Historia
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings
import json
import requests


def check_rol():
    r = requests.get(settings.PATH_LOG, headers={"Accept":"application/json"})
    if r.status_code == 404:
        return False
    else:
        usuario = r.json()
        if usuario["rol"] in ["medico", "medica", "enfermera", "enfermero"]:
            return True
        else:
            return False
def HistoriaList(request):
    if check_rol():
        queryset = Historia.objects.all()
        context = list(queryset.values('id', 'paciente', 'cc'))
        return JsonResponse(context, safe=False)
    return HttpResponse("Usuario actual no autorizado y/o no ingresado", status=403)

def HistoriaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        historia = Historia()
        historia.paciente = data_json["paciente"]
        historia.cc = data_json["cc"]
        historia.save()
        return HttpResponse("Paciente registrado-Nueva historia clínica registrada")
    
def HistoriasCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        historia_list = []
        for historia in data_json:
                dbhistoria = Historia()
                dbhistoria.paciente = historia['paciente']
                dbhistoria.cc = historia['cc']
                historia_list.append(dbhistoria)
        
        Historia.objects.bulk_create(historia_list)
        return HttpResponse("Pacientes registrados-Nuevas historias clínicas registrada") 