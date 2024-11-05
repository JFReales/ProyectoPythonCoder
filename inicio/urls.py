from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('insertar/', views.insertar_mascota, name='insertar_mascota'),  
    path('buscar/', views.MascotaListView.as_view(), name='buscar_mascota'),  
    path('aboutme/', views.aboutme, name='aboutme'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('register/', views.register, name='register'),
     path('perfil/', views.user_profile, name='profile'),
]
