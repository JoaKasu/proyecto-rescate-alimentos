from django.contrib import admin
from .models import Comercio, OrganizacionSocial, Alimento, ReservaDonacion

@admin.register(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    list_display = ('razon_social', 'rut', 'telefono', 'contacto')
    search_fields = ('razon_social', 'rut')

@admin.register(OrganizacionSocial)
class OrganizacionSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre_entidad', 'personalidad_juridica', 'responsable', 'telefono')
    search_fields = ('nombre_entidad', 'personalidad_juridica')

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'comercio', 'categoria', 'cantidad', 'estado', 'fecha_vencimiento')
    list_filter = ('categoria', 'estado', 'fecha_vencimiento')
    search_fields = ('nombre_producto', 'comercio__razon_social')

@admin.register(ReservaDonacion)
class ReservaDonacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'alimento', 'organizacion', 'fecha_reserva', 'completada')
    list_filter = ('completada', 'fecha_reserva')
    search_fields = ('alimento__nombre_producto', 'organizacion__nombre_entidad')