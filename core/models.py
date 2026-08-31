from django.db import models

class Alimento(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    cantidad = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    fecha_limite = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} unidades"