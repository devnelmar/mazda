from django.shortcuts import render, redirect, render_to_response
from propietarios.forms import PropietarioForm
from propietarios.models import Propietario
from vehiculos.models import Vehiculo
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

@login_required
def propietario_list(request):
    q = request.GET.get('q', '')

    querys = (Q(nombre__icontains=q) | Q(identificacion__icontains=q))
    propietario = Propietario.objects.filter(querys)
    contexto = {'propietario': propietario}

    return render(request, 'propietario/propietario_list.html', contexto)



@login_required
def propietario_create(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propietario:propietario_lista')
        else:
            return render(request, 'propietario/propietario_form.html', {'form': form})
    else:
        form = PropietarioForm()
    return render(request, 'propietario/propietario_form.html', {'form': form})


@login_required
def propietario_edit(request, id_propietario):
    propietario = Propietario.objects.get(id=id_propietario)
    vehiculos = Vehiculo.objects.filter(id_propietario=propietario)

    if request.method == "POST":
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
        else:
            print("ERRORS: ", form.errors)
        return redirect('propietario:propietario_lista')
    else:
        form = PropietarioForm(instance=propietario)
    context = {'form': form, 'vehiculos': vehiculos}
    return render(request, 'propietario/propietario_form.html', context)


@login_required
def propietario_delete(request, id_propietario):
    propietario = Propietario.objects.get(id=id_propietario)
    if request.method == 'POST':
        propietario.delete()
        return redirect('propietario:propietario_lista')
    return render(request, 'propietario/propietario_delete.html', {'propietario': propietario})


def busqueda(request):



    querys |= Q(placa__icontains=q)

    vehiculo = Vehiculo.objects.filter(querys)


    context = {'vehiculo': vehiculo, 'propietario': propietario}

    return render(request, 'propietario/propietario_list.html', context)
