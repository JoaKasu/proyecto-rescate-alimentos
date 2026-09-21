from django.contrib import admin
from .models import Comercio, OrganizacionSocial, Alimento, ReservaDonacion

@admin.register(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    list_display = ['razon_social', 'rut_comercial', 'telefono', 'contacto']
    search_fields = ['razon_social', 'rut_comercial']

@admin.register(OrganizacionSocial)
class OrganizacionSocialAdmin(admin.ModelAdmin):
    list_display = ['nombre_entidad', 'personalidad_juridica', 'responsable', 'telefono']
    search_fields = ['nombre_entidad', 'personalidad_juridica']

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'cantidad', 'comercio', 'disponible', 'fecha_limite']
    list_filter = ['categoria', 'disponible']
    search_fields = ['nombre']

@admin.register(ReservaDonacion)
class ReservaDonacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'alimento', 'organizacion', 'estado', 'fecha_reserva']
    list_filter = ['estado']