from django import forms
from .models import Mascota, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'edad', 'imagen']

class BuscarMascotaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar', 'bio', 'date_of_birth']
    


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
    
    
    
    
