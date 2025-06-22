from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail', unique=True)
    telefone = models.CharField('Telefone', max_length=20)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['id']

    def __str__(self):
        return self.nome
