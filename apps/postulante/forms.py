from django import forms
from apps.postulante.models import Postulante

class PostulanteForm(forms.ModelForm):
    class Meta:
        model = Postulante
        fields = [
            'Nombre',
            'Apellidos',
            'Correo',
            'Archivo',
            'Detalle',
            'Entrevista',
            'Notas',
        ]

        labels = {
            'Nombre': 'Nombre',
            'Apellidos':'Apellidos',
            'Correo':'Correo',
            'Archivo':'Archivo',
            'Detalle':'Detalle',
            'Entrevista':'Entrevista',
            'Notas':'Notas',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control'}),
            
            'Detalle': forms.Textarea(attrs={'class': 'form-control'}),
            'Entrevista': forms.Textarea(attrs={'class': 'form-control'}),
            'Notas': forms.TextInput(attrs={'class': 'form-control'}),
        }

    