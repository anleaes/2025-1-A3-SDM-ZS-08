from django.db import models

# Create your models here.

class TecnicoEspecialidade(models.Model):
    tecnico = models.ForeignKey('tecnico.Tecnico', on_delete=models.CASCADE, related_name='especialidades')
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='tecnicos')

    class Meta:
        unique_together = ('tecnico', 'especialidade')

    def __str__(self):
        return f"{self.tecnico} - {self.especialidade}"
