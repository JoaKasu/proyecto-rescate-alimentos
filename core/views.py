from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimento
from .forms import AlimentoForm

def catalogo_alimentos(request):
    alimentos = Alimento.objects.all().order_by('-fecha_publicacion')
    return render(request, 'core/index.html', {'alimentos': alimentos})

def registrar_alimento(request):
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlimentoForm()
    return render(request, 'core/registro.html', {'form': form})

def editar_alimento(request, id):
    alimento = get_object_or_404(Alimento, pk=id)
    if request.method == 'POST':
        form = AlimentoForm(request.POST, instance=alimento)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlimentoForm(instance=alimento)
    return render(request, 'core/editar.html', {'form': form, 'alimento': alimento})

def eliminar_alimento(request, id):
    alimento = get_object_or_404(Alimento, pk=id)
    if request.method == 'POST':
        alimento.delete()
        return redirect('index')
    return render(request, 'core/confirmar_eliminar.html', {'alimento': alimento})