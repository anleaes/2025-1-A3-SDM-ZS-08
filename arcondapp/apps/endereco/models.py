from django.db import models
from usuario.models import Usuario  

class Endereco(models.Model):
    # Definição do seu modelo Endereco
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado}"