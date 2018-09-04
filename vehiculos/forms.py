from django import forms
from vehiculos.models import Vehiculo


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'id_propietario',
            'placa',
            'modelo',
            'tipo_vehiculo',
        ]
        labels = {
            'id_propietario': 'ID de Propietario',
            'placa': 'Placa',
            'modelo': 'Modelo',
            'tipo_vehiculo': 'Tipo de Vehiculo',
        }
        widgets = {
            'id_propietario': forms.Select(attrs={'class': 'form-control'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
        }
