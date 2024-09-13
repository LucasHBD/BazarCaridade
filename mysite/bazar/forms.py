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
                'evento': forms.SelectCheckboxMultiple(attrs={'class':'form-control'}),
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
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "tatuadouro@gmail.com"})
    )
    nome = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "João Tatuador"})
    )
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']
        labels = {
            'nome' : 'Nome',
            'usuario' : 'Nome de Usuario',
            'email' : 'Email',
            'senha' : 'Senha',
            'senha2' : 'Confirme a Senha',
        }
        widgets = {
                'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':'John Eater'}),
                'usuario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'JohnEater2003'}),
                'email': forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'a@b.com'}),
            }
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Usuario.objects.create(
                usuario = user,
                nome=self.cleaned_data['nome_usuario'],
                email=user.email
            )
        return user
