from django.urls import path
from .views import ListaAlvosView, DetalheAlvoView

urlpatterns = [
    path('', ListaAlvosView.as_view(), name='lista_alvos'),
    path('alvo/<int:pk>/', DetalheAlvoView.as_view(), name='detalhe_alvo'),
]
