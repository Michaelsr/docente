from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EvaluadoresForm
from .models import Evaluadores
# Create your views here.

class EvaluadoresList(ListView):
    model = Evaluadores
    template_name = 'evaluadores/evaluadores_list.html'


class EvaluadoresCreate(CreateView):
    model = Evaluadores
    form_class = EvaluadoresForm
    template_name = 'evaluadores/evaluadores_add.html'
    success_url = reverse_lazy('listarevaluadores')


class EvaluadoresUpdate(UpdateView):
    model = Evaluadores
    form_class = EvaluadoresForm
    template_name = 'evaluadores/evaluadores_add.html'
    success_url = reverse_lazy('listarevaluadores')


class EvaluadoresDelete(DeleteView):
    model = Evaluadores
    template_name = 'evaluadores/evaluadores_delete.html'
    success_url = reverse_lazy('listarevaluadores')
