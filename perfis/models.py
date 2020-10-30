from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    class Meta:
        db_table = 'PERFIL'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    nome_empresa = models.CharField(max_length=255)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    @property
    def email(self):
        return self.usuario.email

    def desfazer(self, perfil):
        self.contatos.remove(perfil)
        perfil.contatos.remove(self)

    def pode_convidar(self, perfil):
        nao_pode = self.convite_a_si_mesmo(perfil) or self.ja_eh_contato(perfil) or self.ja_possui_convite(perfil)

        return not nao_pode

    def convite_a_si_mesmo(self, perfil):
        return self == perfil

    def ja_eh_contato(self, perfil):
        return perfil in self.contatos.all()

    def ja_possui_convite(self, perfil):
        return (Convite.objects.filter(solicitante=self, convidado=perfil).exists() or
                Convite.objects.filter(solicitante=perfil, convidado=self).exists())

    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self, convidado=perfil_convidado)
            convite.save()

    def __str__(self):
        return self.nome

    def __repr__(self):
        return self.__str__()


class Convite(models.Model):
    class Meta:
        db_table = 'CONVITE'
        verbose_name = 'convite'
        verbose_name_plural = 'convites'

    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.convidado.contatos.add(self.solicitante)
        self.solicitante.contatos.add(self.convidado)
        self.delete()

    def recusar(self):
        self.delete()

    def __str__(self):
        return str(self.solicitante) + ' - ' + str(self.convidado)

    def __repr__(self):
        return self.__str__()
