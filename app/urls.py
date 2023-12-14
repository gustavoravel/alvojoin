from django.urls import path
from .views import *

urlpatterns = [
    path('', ListaAlvosView.as_view(), name='lista_alvos'),
    path('alvo/<int:pk>/', DetalheAlvoView.as_view(), name='detalhe_alvo'),
    path('alvos/adicionar/', AdicionarAlvoView.as_view(), name='adicionar_alvo'),
    path('alvos/editar/<int:pk>/', EditarAlvoView.as_view(), name='editar_alvo'),
    path('alvos/excluir/<int:pk>/', ExcluirAlvoView.as_view(), name='excluir_alvo'),
]
