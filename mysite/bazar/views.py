from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import *

# Create your views here.

def home(request):
    evento = Evento.objects.all()
    template = loader.get_template('bazar/home.html')
    context = {
        'eventos' : evento
    }
    return render(request, "bazar/home.html", context)

def eventos(request):
    evento = Evento.objects.all()
    context = {
        'evento': evento
    }
    return render(request, "bazar/eventos.html", context)

def itens(request):
    return HttpResponse("Página dos Itens Cadastrados no Evento")