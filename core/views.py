from rest_framework import viewsets
from .models import LoteAlimento, Reserva
from .serializers import LoteAlimentoSerializer, ReservaSerializer

class LoteAlimentoViewSet(viewsets.ModelViewSet):
    queryset = LoteAlimento.objects.all().order_by('-fecha_publicacion')
    serializer_class = LoteAlimentoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by('-fecha_reserva')
    serializer_class = ReservaSerializer