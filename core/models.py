from django.db import models

class Comercio(models.Model):
    razon_social = models.CharField(max_length=150)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return self.razon_social

class OrganizacionSocial(models.Model):
    nombre_entidad = models.CharField(max_length=150)
    personalidad_juridica = models.CharField(max_length=50, unique=True)
    responsable = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_entidad

class Alimento(models.Model):
    CATEGORIAS = [
        ('Panaderia', 'Panadería y Pastelería'),
        ('Frutas', 'Frutas y Verduras'),
        ('Abarrotes', 'Abarrotes y No Perecibles'),
        ('Lacteos', 'Lácteos y Refrigerados'),
    ]

    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Reservado', 'Reservado'),
        ('Entregado', 'Entregado'),
    ]

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE, related_name='alimentos')
    nombre_producto = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    cantidad = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Disponible')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_producto} ({self.cantidad} unidades)"

class ReservaDonacion(models.Model):
    alimento = models.OneToOneField(Alimento, on_delete=models.CASCADE, related_name='reserva')
    organizacion = models.ForeignKey(OrganizacionSocial, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"Reserva #{self.id} - {self.alimento.nombre_producto}"