from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimento, Comercio
from .forms import AlimentoForm, ComercioForm

def catalogo_alimentos(request):
    alimentos = Alimento.objects.all().order_by('-fecha_publicacion')
    return render(request, 'core/catalogo.html', {'alimentos': alimentos})

def registrar_alimento(request):
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = AlimentoForm()
    return render(request, 'core/registro.html', {'form': form})

def editar_alimento(request, id):
    alimento = get_object_or_404(Alimento, pk=id)
    if request.method == 'POST':
        form = AlimentoForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = AlimentoForm(instance=alimento)
    return render(request, 'core/editar.html', {'form': form, 'alimento': alimento})

def eliminar_alimento(request, id):
    alimento = get_object_or_404(Alimento, pk=id)
    if request.method == 'POST':
        alimento.delete()
        return redirect('catalogo')
    return render(request, 'core/confirmar_eliminar.html', {'alimento': alimento})

def registrar_comercio(request):
    if request.method == 'POST':
        form = ComercioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrar_alimento')
    else:
        form = ComercioForm()
    return render(request, 'core/registro_comercio.html', {'form': form})