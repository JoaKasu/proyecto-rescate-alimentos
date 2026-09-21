from django.shortcuts import render, redirect
from .models import Alimento, Comercio

def index(request):
    alimentos = Alimento.objects.select_related('comercio').all()
    total_items = alimentos.count()
    hay_disponibles = total_items > 0

    contexto = {
        'alimentos': alimentos,
        'total_items': total_items,
        'hay_disponibles': hay_disponibles,
    }
    return render(request, 'core/index.html', contexto)

def registrar_alimento(request):
    comercios = Comercio.objects.all()

    if request.method == 'POST':
        comercio_id = request.POST.get('comercio')
        nombre = request.POST.get('nombre', '').strip()
        categoria = request.POST.get('categoria', '').strip()
        cantidad_raw = request.POST.get('cantidad', '0').strip()
        fecha_limite = request.POST.get('fecha_limite', '').strip()

        if nombre and categoria and fecha_limite:
            try:
                cantidad = int(cantidad_raw)
                if cantidad < 0:
                    cantidad = 0
            except ValueError:
                cantidad = 1

            comercio_obj = None
            if comercio_id:
                comercio_obj = Comercio.objects.filter(id=comercio_id).first()

            Alimento.objects.create(
                comercio=comercio_obj,
                nombre=nombre,
                categoria=categoria,
                cantidad=cantidad,
                fecha_limite=fecha_limite,
                disponible=True
            )
            return redirect('index')

    return render(request, 'core/registro.html', {'comercios': comercios})