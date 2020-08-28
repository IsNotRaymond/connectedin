from django.shortcuts import render
from .models import Perfil


def index(request):
    return render(request, 'perfis/index.html')


def exibir(request, id_perfil):
    perfil = Perfil()

    if id_perfil == 1:
        perfil = Perfil(1, 'Elvis', 'elvis@gmail.com', '99999-9999', 'IFPI')
    elif id_perfil == 2:
        perfil = Perfil(2, 'Lucas', 'lucas@gmail.com', '98888-8888', 'UFPI')

    return render(request, 'perfis/perfil.html', {'perfil': perfil})
