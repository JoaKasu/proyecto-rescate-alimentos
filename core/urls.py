from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo_alimentos, name='catalogo'),
    path('registro/', views.registrar_alimento, name='registrar_alimento'),
    path('editar/<int:id>/', views.editar_alimento, name='editar_alimento'),
    path('eliminar/<int:id>/', views.eliminar_alimento, name='eliminar_alimento'),
]