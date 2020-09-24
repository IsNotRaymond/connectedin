from django.db import models


class Usuario(models.Model):
    class Meta:
        db_table = 'USUARIO'
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    email = models.EmailField()
    senha = models.CharField(max_length=200)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.email

    def __repr__(self):
        self.__str__()


class Perfil(models.Model):
    class Meta:
        db_table = 'PERFIL'
        verbose_name = 'perfil'
        verbose_name_plural = 'perfis'

    nome = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def convidar(self, id_convidado):
        pass

    def __str__(self):
        return self.nome

    def __repr__(self):
        self.__str__()


class Contato(models.Model):
    class Meta:
        db_table = 'CONTATO'
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    perfil_principal = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='perfil_principal')
    perfil_adicionado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='perfil_adicionado')

    def __str__(self):
        return str(self.perfil_principal) + ' - ' + str(self.perfil_adicionado)

    def __repr__(self):
        self.__str__()
