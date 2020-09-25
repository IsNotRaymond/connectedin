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

    def convidar(self, perfil_convidado):
        if self.id == perfil_convidado.id:
            return None

        c = Convite(solicitante=self, convidado=perfil_convidado)
        c.save()

        return c

    def __str__(self):
        return self.nome

    def __repr__(self):
        self.__str__()


class Convite(models.Model):
    class Meta:
        db_table = 'CONVITE'
        verbose_name = 'convite'
        verbose_name_plural = 'convites'

    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='perfil_solicitante')
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='perfil_convidado')

    def __str__(self):
        return str(self.solicitante) + ' - ' + str(self.convidado)

    def __repr__(self):
        self.__str__()
