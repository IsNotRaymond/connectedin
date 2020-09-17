from django.db import models
from perfis.models import Perfil


class Postagem(models.Model):
    class Meta:
        db_table = 'POSTAGEM'
        verbose_name = 'postagem'
        verbose_name_plural = 'postagens'

    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return 'Postagem - ' + str(self.texto)

    def __repr__(self):
        self.__str__()


class Comentario(models.Model):
    class Meta:
        db_table = 'COMENTARIO'
        verbose_name = 'comentario'
        verbose_name_plural = 'Comentarios'

    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.perfil) + ' - ' + str(self.texto)

    def __repr__(self):
        self.__str__()


class Tipo(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nome)

    def __repr__(self):
        self.__str__()


class Reacao(models.Model):
    class Meta:
        db_table = 'REACAO'
        verbose_name = 'reacao'
        verbose_name_plural = 'reacoes'

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postagem) + ' - ' + str(self.perfil) + ' - ' + str(self.tipo)

    def __repr__(self):
        self.__str__()

