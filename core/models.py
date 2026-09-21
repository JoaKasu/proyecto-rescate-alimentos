from django.db import models

class Comercio(models.Model):
    razon_social = models.CharField(max_length=120)
    rut_comercial = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.razon_social} ({self.rut_comercial})"


class OrganizacionSocial(models.Model):
    nombre_entidad = models.CharField(max_length=150)
    personalidad_juridica = models.CharField(max_length=50, unique=True)
    responsable = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_entidad


class Alimento(models.Model):
    CATEGORIAS = [
        ('Frutas y Verduras', 'Frutas y Verduras'),
        ('Panadería y Pastelería', 'Panadería y Pastelería'),
        ('Lácteos', 'Lácteos'),
        ('Abarrotes', 'Abarrotes'),
        ('Otros', 'Otros'),
    ]

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, related_name='alimentos', null=True, blank=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    cantidad = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    fecha_limite = models.DateField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad} un.)"


class ReservaDonacion(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente de Retiro'),
        ('Retirado', 'Retirado Conforme'),
        ('Cancelado', 'Cancelado'),
    ]

    alimento = models.ForeignKey(Alimento, on_delete=models.CASCADE, related_name='reservas')
    organizacion = models.ForeignKey(OrganizacionSocial, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_retiro = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Pendiente')
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva #{self.id} - {self.alimento.nombre} -> {self.organizacion.nombre_entidad}"