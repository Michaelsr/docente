from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ComisionForm
from .models import Comision
# Create your views here.

class ComisionList(ListView):
    model = Comision
    template_name = 'comision/comision_list.html'


class ComisionCreate(CreateView):
    model = Comision
    form_class = ComisionForm
    template_name = 'comision/comision_add.html'
    success_url = reverse_lazy('listarComision')


class ClienteUpdate(UpdateView):
    model = Comision
    form_class = ComisionForm
    template_name = 'comision/comision_add.html'
    success_url = reverse_lazy('listarComision')


class ClienteDelete(DeleteView):
    model = Comision
    template_name = 'comision/comision_delete.html'
    success_url = reverse_lazy('listarComision')
