from django.db import models
from django.apps import apps # Esta importação não parece ser usada aqui, pode ser removida se não for necessária.

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', min_length=11)
    

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return self.nome