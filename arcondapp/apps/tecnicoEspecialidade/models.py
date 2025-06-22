from django.db import models

# Create your models here.
class TecnicoEspecialidade(models.Model):
    tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, related_name='especialidades')
    especialidade = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Especialidade de Técnico'
        verbose_name_plural = 'Especialidades de Técnicos'