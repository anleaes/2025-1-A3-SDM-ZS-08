from django.db import models

# Create your models here.

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class TecnicoEspecialidade(models.Model):
    tecnico = models.ForeignKey('tecnico.Tecnico', on_delete=models.CASCADE, related_name='especialidades')
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE, related_name='tecnicos')

    class Meta:
        unique_together = ('tecnico', 'especialidade')

    def __str__(self):
        return f"{self.tecnico} - {self.especialidade}"
