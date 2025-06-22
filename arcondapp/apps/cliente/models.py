from django.db import models
from usuario.models import Usuario

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('Email', unique=True)
    telefone = models.CharField('Telefone', max_length=20)
    endereco = models.CharField('Endereço', max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']