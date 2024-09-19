from django import forms
from django.contrib.auth.models import User
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
            'evento': forms.Select(attrs={'class':'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
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
        
class CriarFormUsuario(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "a@b.com"})
    )
    nome = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Seu Nome"})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Senha"})
    )

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'senha': 'Senha',
        }

    def save(self, commit=True):
        # Cria um objeto User
        username = self.cleaned_data['nome'].replace(" ", "").lower()  # Crie um nome de usuário baseado no nome
        user = User.objects.create_user(
            username=username,
            email=self.cleaned_data['email'],
            password=self.cleaned_data['senha']
        )
        
        if commit:
            # Salva o objeto Usuario
            usuario = super().save(commit=False)
            usuario.usuario = user  # Associa o User ao campo usuario
            usuario.save()
        
        return usuario

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = []  # Deixe os campos em branco pois eles serão preenchidos automaticamente na view
        labels = {}

    def __init__(self, *args, **kwargs):
        # Extraia o argumento item para não precisar incluir no formulário
        self.item = kwargs.pop('item', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        reserva = super().save(commit=False)
        reserva.item = self.item
        reserva.usuario = self.initial.get('usuario', None)  # Aqui você pode definir o usuário, se necessário
        if commit:
            reserva.save()
        return reserva
