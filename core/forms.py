from django import forms
from .models import Alimento, Comercio

# --- Formulario de Alimento (El que ya tenías) ---
class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['comercio', 'nombre_producto', 'categoria', 'cantidad', 'fecha_vencimiento', 'estado']
        widgets = {
            'comercio': forms.Select(attrs={'class': 'form-select'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Marraquetas del día'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = ['razon_social', 'rut', 'direccion', 'telefono', 'contacto']
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Panadería El Maná'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 76.123.456-7'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Av. San Diego 1234'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. +56912345678'}),
            'contacto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del encargado'}),
        }