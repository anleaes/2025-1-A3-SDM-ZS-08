from django.db import models
from usuario.models import Usuario, Cliente
from django.utils import timezone

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)

class Meta:
    verbose_name = 'Endereço'
    verbose_name_plural = 'Endereços'

def __str__(self):
    return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'
