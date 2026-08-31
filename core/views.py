from django.shortcuts import render, redirect
from .models import Alimento

def index(request):
    alimentos = Alimento.objects.all()
    total_items = alimentos.count()
    hay_disponibles = total_items > 0
    
    context = {
        'alimentos': alimentos,
        'total_items': total_items,
        'hay_disponibles': hay_disponibles
    }
    return render(request, 'core/index.html', context)

def registrar_alimento(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = request.POST.get('categoria')
        cantidad = request.POST.get('cantidad')
        fecha_limite = request.POST.get('fecha_limite')

        if nombre and categoria and cantidad and fecha_limite:
            Alimento.objects.create(
                nombre=nombre,
                categoria=categoria,
                cantidad=int(cantidad),
                fecha_limite=fecha_limite,
                disponible=True
            )
            return redirect('index')

    return render(request, 'core/registro.html')