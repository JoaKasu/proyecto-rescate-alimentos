from django import forms
from .models import Alimento

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