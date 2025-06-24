from django.db import models
from .models import Cliente
from .models import Tecnico

# Create your models here.

class Servico(models.Model):
    TIPO_CHOICES = [
        ('Instalação', 'Instalação'),
        ('Manutenção', 'Manutenção'),
        ('Limpeza', 'Limpeza'),
    ]
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Em andamento', 'Em andamento'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')
    data_solicitacao = models.DateTimeField(default=timezone.now)
    data_execucao = models.DateTimeField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='servicos')
    tecnico = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, blank=True, related_name='servicos')