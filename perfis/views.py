from django.shortcuts import render, redirect
from .models import Perfil, Convite


def index(request):
    return render(request, 'perfis/index.html', {'perfis': Perfil.objects.all(),
                                                 'perfil_logado': get_perfil_logado(request)})


def exibir(request, id_perfil):
    perfil = Perfil.objects.get(id=id_perfil)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfis/perfil.html', {'perfil': perfil,
                                                  'perfil_logado': perfil_logado,
                                                  'ja_eh_contato': ja_eh_contato})


def convidar(request, id_perfil):
    perfil_convite = Perfil.objects.get(id=id_perfil)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_convite)

    return redirect('index')


def aceitar(request, id_convite):
    convite = Convite.objects.get(id=id_convite)
    convite.aceitar()

    return redirect('index')


def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
