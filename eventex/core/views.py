"""Modulo responsavel por gerar as views do app core."""
from django.shortcuts import render, get_object_or_404

# Create your views here.
from eventex.core.models import Speaker, Talk, Course


def home(request):
    """Funcao responsavel por gerar a view index da aplicacao."""
    speakers = Speaker.objects.all()

    return render(request, 'index.html', {'speakers': speakers})


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'core/speaker_detail.html', {'speaker': speaker})


def talk_list(request):
    speaker = Speaker(name='Henrique Bastos', slug='henrique-bastos')
    courses = []
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(),
        'courses': Course.objects.all()
    }
    return render(request, 'core/talk_list.html', context)
