from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.eventos, name='eventos'),
    path('itens/', views.itens, name='itens'),
]