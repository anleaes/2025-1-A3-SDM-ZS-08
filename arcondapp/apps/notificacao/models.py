from django.db import models
from cliente.models import Cliente
from tecnico.models import Tecnico
from django.utils import timezone

# Create your models here.
class Notificacao(models.Model):
    DESTINATARIO_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Tecnico', 'Técnico'),
    ]

    destinatario_tipo = models.CharField(max_length=10, choices=DESTINATARIO_CHOICES)
    destinatario_id = models.PositiveIntegerField()
    mensagem = models.TextField()
    data_hora = models.DateTimeField(default=timezone.now)

    def enviar(self):
        print(f'Notificação enviada para {self.destinatario_tipo} #{self.destinatario_id}: {self.mensagem}')