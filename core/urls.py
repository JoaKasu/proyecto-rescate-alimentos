from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoteAlimentoViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'lotes', LoteAlimentoViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]