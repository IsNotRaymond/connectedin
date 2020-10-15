from django.db import models


class Perfil(models.Model):
    class Meta:
        db_table = 'PERFIL'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    nome_empresa = models.CharField(max_length=255)

    contatos = models.ManyToManyField('self')

    def convidar(self, perfil_convidado):
        if self.id == perfil_convidado.id:
            return None

        try:
            Convite.objects.get(solicitante=self, convidado=perfil_convidado)
            return None

        except Convite.DoesNotExist:
            c = Convite(solicitante=self, convidado=perfil_convidado)
            c.save()

            return c

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

    def __str__(self):
        return str(self.solicitante) + ' - ' + str(self.convidado)

    def __repr__(self):
        return self.__str__()
