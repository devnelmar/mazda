from django import forms

from propietarios.models import Propietario


class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = [
            'nombre',
            'sexo',
            'edad',
            'identificacion',
            'email',
            'telefono'
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad': 'Edad',
            'identificacion': 'Identificacion',
            'email': 'Email',
            'telefono': 'Telefono'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'})
        }
