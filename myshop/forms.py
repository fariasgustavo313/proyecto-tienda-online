from django import forms
from django.forms import ModelForm
from .models import Remera

class FormularioRemera(ModelForm):
    class Meta:
        model = Remera
        fields = ("marca", "talle", "color", "lisa", "genero")
        
class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Tu nombre'
    }))
    email = forms.EmailField(label="Correo electrónico", widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'tu@email.com'
    }))
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Escribí tu mensaje aquí...'
    }))