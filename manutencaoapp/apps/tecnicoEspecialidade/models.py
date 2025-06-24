from django.db import models

# Create your models here.

from django.db import models

class TecnicoEspecialidade(models.Model):
    tecnico = models.ForeignKey('tecnico.Tecnico', on_delete=models.CASCADE, related_name='especialidades')
    nome_especialidade = models.CharField(max_length=100)

    class Meta:
        unique_together = ('tecnico', 'nome_especialidade')

    def __str__(self):
        return f"{self.tecnico} - {self.nome_especialidade}"
