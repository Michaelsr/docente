from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Parevaluador

class ParevaluadorForm(forms.ModelForm):
    class Meta: 
        fields = [
            'Comision',
            'Detalle',
            'Pareva',
            'Nota',
        ]
        
        labels = {
            'Comision':'comision',
            'Detalle':'Detalle',
            'Pareva':'Numero evaluacion',
            'Nota':'Nota',
        }

        widgets = {
            'Comision': forms.Select(attrs={'class': 'form-control'}),
            'Detalle': forms.TextInput(attrs={'class': 'form-control'}),
            'Pareva': forms.TextInput(attrs={'class': 'form-control'}),
            'Nota': forms.TextInput(attrs={'class': 'form-control'}),
        }