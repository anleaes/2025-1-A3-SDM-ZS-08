from django.db import models

# Create your models here.

class Endereco(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, related_name='enderecos')

    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Ex: 'SP', 'RJ'
    cep = models.CharField(max_length=9)     # Ex: '12345-678'

    referencia = models.CharField(max_length=255, blank=True, null=True)
    principal = models.BooleanField(default=False)  # Se é o endereço principal do cliente

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"
