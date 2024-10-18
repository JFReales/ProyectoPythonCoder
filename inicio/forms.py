from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'edad', 'propietario']

class BuscarMascotaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
