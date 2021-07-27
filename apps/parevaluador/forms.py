from django import forms
from .models import Parevaluador

class ParevaluadorForm(forms.ModelForm):
    class Meta: 
        model = Parevaluador
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