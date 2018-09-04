from django.shortcuts import render, redirect
from vehiculos.forms import VehiculoForm
from vehiculos.models import Vehiculo
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required
def index(request):
    return render(request, 'vehiculo/index.html')


@login_required
def vehiculo_list(request):
    q = request.GET.get('q', '')
    querys = (Q(placa__icontains=q) | Q(modelo__icontains=q))
    vehiculo = Vehiculo.objects.filter(querys)

    contexto = {'vehiculo': vehiculo}

    return render(request, 'vehiculo/vehiculo_list.html', contexto)


@login_required
def vehiculo_create(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:vehiculo_lista')
        else:
            return render(request, 'vehiculo/vehiculo_form.html', {'form': form})
    else:
        form = VehiculoForm()
    return render(request, 'Vehiculo/vehiculo_form.html', {'form': form})


@login_required
def vehiculo_edit(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id=id_vehiculo)
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
        else:
            print("ERRORS: ", form.errors)
        return redirect('vehiculo:vehiculo_lista')
    else:
        form = VehiculoForm(instance=vehiculo)
    return render(request, 'vehiculo/vehiculo_form.html', {'form': form})


@login_required
def vehiculo_delete(request, id_vehiculo):
    vehiculo = Vehiculo.objects.get(id=id_vehiculo)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('vehiculo:vehiculo_lista')
    return render(request, 'vehiculo/vehiculo_delete.html', {'vehiculo': vehiculo})
