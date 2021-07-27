from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ParevaluadorForm
from .models import Parevaluador
# Create your views here.

class ParevaList(ListView):
    model = Parevaluador
    template_name = 'parevaluador/par_list.html'


class ParevaCreate(CreateView):
    model = Parevaluador
    form_class = ParevaluadorForm
    template_name = 'parevaluador/par_add.html'
    success_url = reverse_lazy('listarparevaluador')


class ParevaUpdate(UpdateView):
    model = Parevaluador
    form_class = ParevaluadorForm
    template_name = 'parevaluador/par_add.html'
    success_url = reverse_lazy('listarparevaluador')


class ParevaDelete(DeleteView):
    model = Parevaluador
    template_name = 'parevaluador/par_delete.html'
    success_url = reverse_lazy('listarparevaluador')

