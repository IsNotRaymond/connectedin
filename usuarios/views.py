from django.shortcuts import render
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil
from django.shortcuts import redirect


class RegistrarUsuarioView(View):

    def get(self, request):
        return render(request, 'registrar.html')

    def post(self, request):
        form = RegistrarUsuarioForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            usuario = User.objects.create_user(dados['nome'],
                                               dados['email'],
                                               dados['senha'])

            perfil = Perfil(nome=usuario.username,
                            nome_empresa=dados['nome_empresa'],
                            telefone=dados['telefone'],
                            usuario=usuario)
            perfil.save()
            return redirect('index')

        return render(request, 'registrar.html', {'form': form})
