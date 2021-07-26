from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostulanteForm
from .models import Postulante
# Create your views here.

class PostulanteList(ListView):
    model = Postulante
    template_name = 'postulante/postulante_list.html'

class PostulanteCreate(CreateView):
    model = Postulante
    form_class = PostulanteForm
    template_name = 'postulante/postulante_add.html'
    success_url = reverse_lazy('listarPostulante')
    
class PostulanteUpdate(UpdateView):
    model = Postulante
    form_class = PostulanteForm
    template_name = 'postulante/postulante_add.html'
    success_url = reverse_lazy('listarPostulante')

class PostulanteDelete(DeleteView):
    model = Postulante
    template_name = 'postulante/postulante_delete.html'
    success_url = reverse_lazy('listarPostulante')