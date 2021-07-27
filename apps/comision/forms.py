from django import forms
from django.forms import fields, widgets
from .models import Comision

class ComisionForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = [
            'Postulante',
            'Entrevista',
            'Nota',
            'Detalles',
        ]

        labels ={
            'Postulante':'Postulante',
            'Entrevista':'Entrevista',
            'Nota':'Nota',
            'Detalles':'Detalle',
        }
        widgets = {
            'Postulante': forms.TextInput(attrs={'class': 'form-control'}),
            'Entrevista': forms.TextInput(attrs={'class': 'form-control'}),
            'Nota': forms.TextInput(attrs={'class': 'form-control'}),
            'Detalles': forms.TextInput(attrs={'class': 'form-control'}),
        }