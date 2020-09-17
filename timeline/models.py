from django.db import models
from perfis.models import Perfil
from postagem.models import Postagem


class Timeline(models.Model):
    class Meta:
        db_table = 'TIMELINE'
        verbose_name = 'timeline'
        verbose_name_plural = 'timelines'

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    def __str__(self):
        return 'Timeline - ' + str(self.perfil)

    def __repr__(self):
        self.__str__()


class TimelinePostagem(models.Model):
    class Meta:
        db_table = 'TIMELINE_POSTAGEM'
        verbose_name = 'postagem da Timeline'
        verbose_name_plural = 'postagens da Timeline'

    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return 'TimelinePostagem - ' + str(self.timeline)

    def __repr__(self):
        self.__str__()
