from django.shortcuts import render
from .models import Perfil, Usuario


def index(request):
    return render(request, 'perfis/index.html', {'perfis': Perfil.objects.all(), 'usuarios': Usuario})


def exibir(request, id_perfil):
    perfil = Perfil.objects.get(id=id_perfil)

    return render(request, 'perfis/perfil.html', {'perfil': perfil})


def convidar(request, id_perfil):
    pass
