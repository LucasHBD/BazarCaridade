from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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

@login_required
def itens(request):
    if request.method == "POST":
        form = CriarFormItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('eventos'))  # Redireciona para a página de eventos
        else:
            # Se o formulário não for válido, ele recarrega a página e exibe os erros
            context = {'form': form}
            return render(request, "bazar/itens.html", context)
    else:
        form = CriarFormItem()
        context = {'form': form}
        return render(request, "bazar/itens.html", context)

@login_required
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

def cadastro(request):
    form = CriarFormUsuario()
    submitted = False
    if request.method == "POST":
        form = CriarFormUsuario(request.POST)

        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            user = authenticate(username=nome, password=senha)
            login(request, user)
            return HttpResponseRedirect("/bazar/eventos?submitted = True")
    else:
        form = CriarFormUsuario()
        if "submitted" in request.GET:
            submitted = True
    context = {"form": form, "submitted": submitted}
    return render(request, "bazar/cadastro.html", context)

def reserva(request):
    return render(request, "bazar/reserva.html", context)