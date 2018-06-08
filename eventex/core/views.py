"""Modulo responsavel por gerar as views do app core."""
from django.shortcuts import render

# Create your views here.


def home(request):
    """Funcao responsavel por gerar a view index da aplicacao."""
    return render(request, 'index.html')
