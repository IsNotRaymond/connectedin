from django.shortcuts import render, redirect
from .models import Perfil


def index(request):
    return render(request, 'perfis/index.html', {'perfis': Perfil.objects.all()})


def exibir(request, id_perfil):
    return render(request, 'perfis/perfil.html', {'perfil': Perfil.objects.get(id=id_perfil)})


def convidar(request, id_perfil):
    perfil_convite = Perfil.objects.get(id=id_perfil)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convite)

    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
