from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.eventos, name='eventos'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('itens/', views.itens, name='itens'),
    path('reserva/<int:item_id>/', views.reserva, name='reserva'),
    path('cadastrarevento/', views.cadastrarevento, name='cadastrarevento'),
    path('itemevento/<int:evento_id>/', views.itemevento, name='itemevento'),
    path('evento/<int:evento_id>/itens/', views.BuscarItem.as_view(), name='buscar_item'),
]