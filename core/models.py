from django.db import models

class Usuario(models.Model):
    nome = models.CharField(
        "Nome do Usuário", max_length=80, null=False, blank=False)
    nascimento = models.DateField("Data de Nascimento", null=False, blank=False)
    cpf = models.CharField(
        "CPF", max_length=11, null=False, blank=False
    )
    email = models.EmailField("Email", null=False, blank=False, unique=True)
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome




