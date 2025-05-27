from .models import Historia
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def HistoriaList(request):
    queryset = Historia.objects.all()
    context = list(queryset.values('id', 'paciente', 'cc'))
    return JsonResponse(context, safe=False)

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