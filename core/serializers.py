from rest_framework import serializers
from .models import LoteAlimento, Reserva

class LoteAlimentoSerializer(serializers.ModelSerializer):
    comercio_username = serializers.ReadOnlyField(source='comercio.username')

    class Meta:
        model = LoteAlimento
        fields = [
            'id',
            'titulo',
            'descripcion',
            'cantidad',
            'unidad_medida',
            'fecha_limite_retiro',
            'estado',
            'comercio',
            'comercio_username',
            'fecha_publicacion'
        ]

class ReservaSerializer(serializers.ModelSerializer):
    organizacion_username = serializers.ReadOnlyField(source='organizacion.username')
    lote_titulo = serializers.ReadOnlyField(source='lote.titulo')

    class Meta:
        model = Reserva
        fields = [
            'id',
            'lote',
            'lote_titulo',
            'organizacion',
            'organizacion_username',
            'fecha_reserva',
            'estado'
        ]