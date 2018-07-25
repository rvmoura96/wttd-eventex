"""Modulo responsavel por gerar as views do app core."""
from django.shortcuts import render

# Create your views here.


def home(request):
    """Funcao responsavel por gerar a view index da aplicacao."""
    speakers = [
        {'name': 'Grace Hopper', 'photo': 'http://hbn.link/hopper-pic'},
        {'name': 'Alan Turing', 'photo': 'http://hbn.link/turing-pic'},
    ]
    return render(request, 'index.html', {'speakers': speakers})
