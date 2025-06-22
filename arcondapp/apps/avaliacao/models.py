from django.db import models
from cliente.models import Cliente
from tecnico.models import Tecnico

# Create your models here.
class Avaliacao(models.Model):
    nota = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'