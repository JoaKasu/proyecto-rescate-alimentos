from django.contrib import admin
from .models import Alimento

class AlimentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'cantidad', 'disponible', 'fecha_limite']

admin.site.register(Alimento, AlimentoAdmin)