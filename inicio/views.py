from django.dispatch import receiver
from django.shortcuts import render, redirect
from .forms import MascotaForm, UserProfileForm, UserForm
from .models import Mascota, User, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models.signals import post_save

@login_required
def user_profile(request):
    profile = request.user.userprofile  # Instancia de UserProfile
    user = request.user  # Instancia del User
    
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=user)  # Form para actualizar User
        
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('profile')  # Redirige después de guardar
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=user)
    
    return render(request, 'user_profile.html', {
        'profile_form': profile_form,
        'user_form': user_form,
        'profile': profile,
    })

@login_required
def insertar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('inicio')  
    else:
        form = MascotaForm()  
    return render(request, 'insertar_mascota.html', {'form': form})

@login_required
class MascotaListView(ListView):
    model = Mascota
    template_name = 'buscar_mascota.html'
    context_object_name = 'mascotas' 

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. ¡Bienvenido!')
            return redirect('inicio')  
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class MascotaListView(LoginRequiredMixin, ListView):
    model = Mascota
    template_name = 'buscar_mascota.html'
    context_object_name = 'mascotas'

def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'inicio.html')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def aboutme(request):
    return render(request, 'aboutme.html')
