from django.db import models
from perfis.models import Perfil


class Postagem(models.Model):
    class Meta:
        db_table = 'POSTAGEM'
        verbose_name = 'postagem'
        verbose_name_plural = 'postagens'

    nome_postagem = models.CharField(max_length=255)
    texto = models.TextField()
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_postagem

    def __repr__(self):
        return self.__str__()
