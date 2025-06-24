from django.db import models
from django.utils import timezone

# Create your models here.

class Avaliacao(models.Model):
    AVALIADOR_CHOICES = [
        ('cliente', 'Cliente'),
        ('tecnico', 'Técnico'),
    ]

    avaliador_tipo = models.CharField(max_length=10, choices=AVALIADOR_CHOICES)
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, related_name='avaliacoes_recebidas')
    tecnico = models.ForeignKey('tecnico.Tecnico', on_delete=models.CASCADE, related_name='avaliacoes_recebidas')
    
    nota = models.PositiveSmallIntegerField()  # Ex: 1 a 5 estrelas
    comentario = models.TextField(blank=True)
    data_avaliacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.avaliador_tipo.title()} avaliou com {self.nota} estrela(s)"
