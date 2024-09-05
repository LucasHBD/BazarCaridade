from django import forms
from .models import *

class CriarFormItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'imagem', 'descricao', 'preco']
        labels = {
            'nome' : '',
            'imagem' : '',
            'descricao' : '',
            'preco' : '',
        }
        widgets = {
                'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do Item'}),
                'descricao': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descrição do Item'}),
                'preco': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'0,00'}),
            }

