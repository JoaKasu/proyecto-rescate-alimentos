from django.db import models
from django.contrib.auth.models import User

class LoteAlimento(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('RETIRADO', 'Retirado'),
        ('EXPIRADO', 'Expirado'),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField(help_text="Cantidad del producto")
    unidad_medida = models.CharField(max_length=50, help_text="Ej: kg, unidades, bolsas")
    fecha_limite_retiro = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='DISPONIBLE')
    comercio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lotes')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.cantidad} {self.unidad_medida} ({self.estado})"


class Reserva(models.Model):
    ESTADO_RESERVA = [
        ('PENDIENTE', 'Pendiente de Retiro'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    lote = models.OneToOneField(LoteAlimento, on_delete=models.CASCADE, related_name='reserva')
    organizacion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADO_RESERVA, default='PENDIENTE')

    def __str__(self):
        return f"Reserva de {self.lote.titulo} por {self.organizacion.username}"