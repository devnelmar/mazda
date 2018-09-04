from django.urls import path
from vehiculos.views import index, vehiculo_create, vehiculo_list, vehiculo_edit, vehiculo_delete

app_name = 'vehiculo'

urlpatterns = [
    path('vehiculo/', index, name='index'),
    path('vehiculo/crear', vehiculo_create, name='vehiculo_crear'),
    path('vehiculo/lista', vehiculo_list, name='vehiculo_lista'),
    path('vehiculo/editar/<id_vehiculo>', vehiculo_edit, name='vehiculo_editar'),
    path('vehiculo/eliminar/<id_vehiculo>', vehiculo_delete, name='vehiculo_eliminar'),
]
