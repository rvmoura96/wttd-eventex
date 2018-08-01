"""Modulo responsavel por gerar as views do app core."""
from django.shortcuts import render, get_object_or_404

# Create your views here.
from eventex.core.models import Speaker


def home(request):
    """Funcao responsavel por gerar a view index da aplicacao."""
    speakers = Speaker.objects.all()

    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})