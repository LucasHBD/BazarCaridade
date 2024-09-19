from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import ListView
from django.contrib import messages

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
    evento = get_object_or_404(Evento, id=evento_id)
    itens = Item.objects.filter(evento=evento)
    
    # Verifica se cada item foi reservado pelo usuário
    itens_info = []
    for item in itens:
        reservado = Reserva.objects.filter(item=item, usuario=request.user).exists()
        itens_info.append({
            'item': item,
            'reservado': reservado
        })
    
    context = {
        'evento': evento,
        'itens': itens_info
    }
    return render(request, 'bazar/itemevento.html', context)

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

@login_required
def reserva(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ReservaForm()
    submitted = False

    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.item = item
            reserva.usuario = request.user  # Adiciona o usuário atual
            reserva.save()
            return redirect('itemevento', evento_id=item.evento.id)

    context = {
        'form': form,
        'item': item,
        'submitted': submitted
    }
    return render(request, 'bazar/reserva.html', context)

class BuscarItem(ListView):
    model = Item
    context_object_name = "itens"
    template_name = "bazar/itemevento.html"

    def get_queryset(self):
        evento_id = self.kwargs.get("evento_id")
        query = self.request.GET.get("item", "")

        evento = get_object_or_404(Evento, id=evento_id)
        
        itens = Item.objects.filter(evento=evento)

        if query:
            itens = itens.filter(nome__icontains=query)

        return itens

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        evento_id = self.kwargs.get("evento_id")

        # Adiciona o evento ao contexto
        evento = get_object_or_404(Evento, id=evento_id)
        context["evento"] = evento
        return context
