from django.db import models
from django.contrib.auth.models import User
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
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    evento = models.ForeignKey("Evento", on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=100, null=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=30, null=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if (self.usuario.is_staff == True or self.usuario.is_superuser == True):
            admin_group, created = Group.objects.get_or_create(name='Admin')
            self.usuario.groups.add(admin_group)
        else:
            self.usuario.is_staff = False
            self.usuario.is_superuser = False
            admin_group = Group.objects.filter(name='Admin').first()
            if admin_group:
                self.usuario.groups.remove(admin_group)
        
        self.usuario.save(update_fields=['is_staff', 'is_superuser'])

    def __str__(self):
        return self.nome
    
    
