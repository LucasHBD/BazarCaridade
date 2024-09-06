from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.eventos, name='eventos'),
    path('itens/', views.itens, name='itens'),
    path('cadastrarevento/', views.cadastrarevento, name='cadastrarevento'),
    path('itemevento/<int:evento_id>/', views.itemevento, name='itemevento'),
]