from django.shortcuts import render, redirect
from .forms import MascotaForm, BuscarMascotaForm
from .models import Mascota

from django.shortcuts import render, redirect
from .forms import MascotaForm

def insertar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('inicio')  
    else:
        form = MascotaForm()  
    return render(request, 'insertar_mascota.html', {'form': form})


def buscar_mascota(request):
    form = BuscarMascotaForm()
    resultado = None

    if request.method == 'POST':
        form = BuscarMascotaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultado = Mascota.objects.filter(nombre__icontains=nombre)

    return render(request, 'buscar_mascota.html', {'form': form, 'resultado': resultado})

def inicio(request):
    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'aboutme.html')

