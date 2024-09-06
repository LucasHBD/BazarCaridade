from django import forms
from .models import *

class CriarFormItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'imagem', 'descricao', 'preco', 'evento']
        labels = {
            'nome' : '',
            'imagem' : '',
            'descricao' : '',
            'preco' : '',
            'evento' : '',
        }
        widgets = {
                'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Item'}),
                'descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descrição do Item'}),
                'preco': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'0,00'}),
                'evento': forms.CheckboxInput(attrs={'class':'form-control'}),
            }

class CriarFormEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'evento_inicio', 'evento_fim']
        labels = {
            'nome' : '',
            'evento_inicio' : '',
            'evento_fim' : '',
        }
        widgets = {
                'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Item'}),
                'evento_inicio': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Data de Inicio'}),
                'evento_fim': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Data de Fim'}),
            }

