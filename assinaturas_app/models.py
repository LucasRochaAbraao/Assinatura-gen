from django.db import models
from django.contrib.auth.models import User


class Assinatura(models.Model):
    #user = models.ForeignKey(
    #    User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Usuário")
    nome = models.TextField(null=True, blank=True, verbose_name="Nome Completo")
    setor = models.TextField(null=True, blank=True, verbose_name="Setor")
    telefone = models.TextField(null=True, blank=True, verbose_name="Telefone")
    email = models.TextField(null=True, blank=True, verbose_name="Email")
    
    def __str__(self):
        return self.nome

