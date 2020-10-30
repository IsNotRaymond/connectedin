from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from .forms import CriarPostagemForm
from .models import Postagem
from django.contrib.auth.decorators import login_required
from perfis.views import get_perfil_logado


class CriarPostagem(View):
    @staticmethod
    def get(request):
        return render(request, 'criar_postagem.html', {'perfil_logado': get_perfil_logado(request)})

    @staticmethod
    def post(request):
        form = CriarPostagemForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            postagem = Postagem(nome_postagem=dados['nome_postagem'],
                                texto=dados['texto'],
                                perfil=get_perfil_logado(request))
            postagem.save()
            return redirect('index')

        return render(request, 'criar_postagem.html', {'form': form})

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(self.__class__, self).dispatch(request, *args, **kwargs)


@login_required
def postagens(request):
    perfil_logado = get_perfil_logado(request)
    perfis_contatos = perfil_logado.contatos.all()

    p1 = Postagem.objects.filter(perfil=perfil_logado)
    p2 = Postagem.objects.filter(perfil__in=perfis_contatos)

    all_postagens = p1.union(p2)
    all_postagens = all_postagens.order_by('-data_de_criacao')

    return render(request, 'timeline.html', {'postagens': all_postagens,
                                             'perfil_logado': get_perfil_logado(request)})

@login_required
def detail_postagem(request, id_postagem):
    return render(request, 'postagem.html', {'postagem': Postagem.objects.get(id=id_postagem),
                                             'perfil_logado': get_perfil_logado(request)})
