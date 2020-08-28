from django.db import models


class Perfil(object):
    def __init__(self, id_perfil=0, nome='', email='', telefone='', nome_empresa=''):
        self.id_perfil = id_perfil
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa
