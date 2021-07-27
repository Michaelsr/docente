from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Evaluadores

class EvaluadoresForm(forms.ModelForm):
    class Meta:
        model = Evaluadores
        fields = [
            'Parevaluador',
            'Notasfinal',
            'Detallefin',
        ]

        labels = {
            'Parevaluador':'Evaluador',
            'Notasfinal':'Nota Final',
            'Detallefin':'Detalle Final',
        }

        widgets = {
            'Parevaluador': forms.Select(attrs={'class': 'form-control'}),
            'Notasfinal': forms.TextInput(attrs={'class': 'form-control'}),
            'Detallefin': forms.Textarea(attrs={'class': 'form-control'}),
        }
        