from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Perfil, Convite


@login_required
def index(request):
    return render(request, 'perfis/index.html', {'perfis': Perfil.objects.all(),
                                                 'perfil_logado': get_perfil_logado(request)})


@login_required
def exibir(request, id_perfil):
    perfil = Perfil.objects.get(id=id_perfil)
    perfil_logado = get_perfil_logado(request)
    ja_eh_contato = perfil_logado.ja_eh_contato(perfil)
    return render(request, 'perfis/perfil.html', {'perfil': perfil,
                                                  'perfil_logado': get_perfil_logado(request),
                                                  'ja_eh_contato': ja_eh_contato})


@login_required
def convidar(request, id_perfil):
    perfil_a_convidar = Perfil.objects.get(id=id_perfil)
    perfil_logado = get_perfil_logado(request)

    if perfil_logado.pode_convidar(perfil_a_convidar):
        perfil_logado.convidar(perfil_a_convidar)

    return redirect('index')


@login_required
def aceitar(request, id_convite):
    convite = Convite.objects.get(id=id_convite)
    convite.aceitar()

    return redirect('index')

@login_required
def recusar(request, id_convite):
    convite = Convite.objects.get(id=id_convite)
    convite.recusar()

    return redirect('index')


@login_required
def desfazer(request, id_perfil):
    perfil = Perfil.objects.get(id=id_perfil)
    perfil.desfazer(get_perfil_logado(request))

    return redirect('index')


@login_required
def get_perfil_logado(request):
    return request.user.perfil
