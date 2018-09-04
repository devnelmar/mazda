from django.urls import path
from propietarios.views import propietario_create, propietario_list, propietario_edit, propietario_delete

app_name = 'propietario'

urlpatterns = [
    path('propietario/crear', propietario_create, name='propietario_crear'),
    path('propietario/lista', propietario_list, name='propietario_lista'),
    path('propietario/editar/<id_propietario>', propietario_edit, name='propietario_editar'),
    path('propietario/eliminar/<id_propietario>', propietario_delete, name='propietario_eliminar'),
]
