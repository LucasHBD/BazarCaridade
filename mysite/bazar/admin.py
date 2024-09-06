from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Usuario)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
admin.site.register(Evento, EventoAdmin)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
admin.site.register(Item, ItemAdmin)
