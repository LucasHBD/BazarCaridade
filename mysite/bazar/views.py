from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import loader

from .models import *
from .forms import *

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
    submitted = False
    if request.method == "POST":
        form = CriarFormItem(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bazar/eventos')
    else:
        form = CriarFormItem()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form' : form,
        'submitted' : submitted
    }
    return render(request, "bazar/itens.html", context)

def cadastrarevento(request):
    submitted = False
    if request.method == "POST":
        form = CriarFormEvento(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bazar/eventos')
    else:
        form = CriarFormEvento()
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'form' : form,
        'submitted' : submitted
    }
    return render(request, "bazar/cadastrarevento.html", context)

def itemevento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)

    itens = Item.objects.filter(evento=evento)

    context = {
        'evento': evento,
        'itens': itens
    }
    
    return render(request, "bazar/itemevento.html", context)