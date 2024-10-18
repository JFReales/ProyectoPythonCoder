from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('insertar/', views.insertar_mascota, name='insertar_mascota'),  
    path('buscar/', views.buscar_mascota, name='buscar_mascota'),  
    path('aboutme/', views.aboutme, name='aboutme'), 
]
