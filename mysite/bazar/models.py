from django.db import models

# Create your models here.

def upload_image_item(instance, filename):
    return f"{instance.nome} - {filename}"

class Evento(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    evento_inicio = models.CharField(max_length=5, blank=True, null=True)
    evento_fim = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.nome

class Item(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    imagem = models.ImageField(upload_to=upload_image_item, blank=True, null=False)
    descricao = models.CharField(max_length=200, null=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome
    
    
