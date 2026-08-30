from django.contrib import admin
from .models import LoteAlimento, Reserva

@admin.register(LoteAlimento)
class LoteAlimentoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cantidad', 'unidad_medida', 'estado', 'comercio', 'fecha_limite_retiro')
    list_filter = ('estado', 'fecha_limite_retiro')
    search_fields = ('titulo', 'descripcion')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('lote', 'organizacion', 'fecha_reserva', 'estado')
    list_filter = ('estado', 'fecha_reserva')