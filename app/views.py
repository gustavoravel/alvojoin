from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Alvo

class ListaAlvosView(ListView):
    """
    View que renderiza uma lista de alvos.

    Atributos:
    - `model`: O modelo de dados usado para recuperar os alvos.
    - `template_name`: O nome do template usado para renderizar a lista de alvos.

    Template:
    - `lista_alvos.html`: Este template é usado para exibir a lista de alvos.
    """
    model = Alvo
    template_name = 'lista_alvos.html'

class DetalheAlvoView(DetailView):
    """
    View que exibe os detalhes de um alvo específico.

    Atributos:
    - `model`: O modelo de dados usado para recuperar os detalhes do alvo.
    - `template_name`: O nome do template usado para renderizar os detalhes do alvo.

    URL:
    - A URL para acessar esta view deve incluir um parâmetro de chave primária (pk) que identifica
      o alvo específico. Por exemplo: `/alvos/detalhe/1/`.

    Template:
    - `detalhe_alvo.html`: Este template é usado para exibir os detalhes do alvo.    
    """
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
    """
    View para adicionar um novo alvo.

    Atributos:
    - `model`: O modelo de dados usado para criar um novo alvo.
    - `template_name`: O nome do template usado para renderizar o formulário de adição de alvo.
    - `form_class`: A classe do formulário associada ao modelo de alvo.
    - `success_url`: A URL para redirecionar após a adição bem-sucedida de um novo alvo.

    URL:
    - A URL para acessar esta view deve ser configurada nas urls do Django, por exemplo, usando `path('alvos/adicionar/', AdicionarAlvoView.as_view(), name='adicionar_alvo')`.

    Template:
    - `formulario_alvo.html`: Este template é usado para renderizar o formulário de adição de alvo.
    """
    model = Alvo
    template_name = 'formulario_alvo.html'
    form_class = AlvoForm
    success_url = reverse_lazy('lista_alvos')

class EditarAlvoView(UpdateView):
    """
    View para editar um alvo existente.

    Atributos:
    - `model`: O modelo de dados usado para editar um alvo existente.
    - `template_name`: O nome do template usado para renderizar o formulário de edição de alvo.
    - `form_class`: A classe do formulário associada ao modelo de alvo.
    - `fields`: Os campos do modelo de alvo que devem ser exibidos no formulário.
    - `success_url`: A URL para redirecionar após a edição bem-sucedida de um alvo existente.

    URL:
    - A URL para acessar esta view deve ser configurada nas urls do Django, por exemplo, usando `path('alvos/editar/<int:pk>/', EditarAlvoView.as_view(), name='editar_alvo')`.

    Template:
    - `formulario_alvo.html`: Este template é usado para renderizar o formulário de edição de alvo.
    """
    model = Alvo
    template_name = 'formulario_alvo.html'
    fields = ['identificador', 'nome', 'latitude', 'longitude', 'data_expiracao']
    success_url = reverse_lazy('lista_alvos')

class ExcluirAlvoView(DeleteView):
    """
    View para excluir um alvo.

    Atributos:
    - `model`: O modelo de dados usado para excluir um alvo.
    - `template_name`: O nome do template usado para renderizar a confirmação de exclusão.
    - `success_url`: A URL para redirecionar após a exclusão bem-sucedida de um alvo.

    URL:
    - A URL para acessar esta view deve ser configurada nas urls do Django, por exemplo, usando `path('alvos/excluir/<int:pk>/', ExcluirAlvoView.as_view(), name='excluir_alvo')`.

    Template:
    - `alvo_confirm_delete.html`: Este template é usado para renderizar a confirmação de exclusão de alvo.
    """
    model = Alvo
    success_url = reverse_lazy('lista_alvos')

