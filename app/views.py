from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Alvo

class ListaAlvosView(ListView):
    model = Alvo
    template_name = 'lista_alvos.html'

class DetalheAlvoView(DetailView):
    model = Alvo
    template_name = 'detalhe_alvo.html'

class AlvoForm(forms.ModelForm):
    class Meta:
        model = Alvo
        fields = ['identificador', 'nome', 'latitude', 'longitude', 'data_expiracao']
        widgets = {
            'data_expiracao': forms.DateInput(format=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']),
        }

class AdicionarAlvoView(CreateView):
    model = Alvo
    template_name = 'formulario_alvo.html'
    form_class = AlvoForm
    success_url = reverse_lazy('lista_alvos')

class EditarAlvoView(UpdateView):
    model = Alvo
    template_name = 'formulario_alvo.html'
    fields = ['identificador', 'nome', 'latitude', 'longitude', 'data_expiracao']
    success_url = reverse_lazy('lista_alvos')

class ExcluirAlvoView(DeleteView):
    model = Alvo
    success_url = reverse_lazy('lista_alvos')

