from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Alvo

class ListaAlvosView(ListView):
    model = Alvo
    template_name = 'lista_alvos.html'

class DetalheAlvoView(DetailView):
    model = Alvo
    template_name = 'detalhe_alvo.html'

class AdicionarAlvoView(CreateView):
    model = Alvo
    template_name = 'formulario_alvo.html'
    fields = ['identificador', 'nome', 'latitude', 'longitude', 'data_expiracao']

class EditarAlvoView(UpdateView):
    model = Alvo
    template_name = 'formulario_alvo.html'
    fields = ['identificador', 'nome', 'latitude', 'longitude', 'data_expiracao']

class ExcluirAlvoView(DeleteView):
    model = Alvo
    success_url = reverse_lazy('lista_alvos')

