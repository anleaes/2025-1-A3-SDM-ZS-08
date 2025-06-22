from django.db import models
from usuario.models import Usuario
from django.utils import timezone
# from cliente.models import Cliente 

# Create your models here.

class Tecnico(Usuario):
    avaliacao_media = models.FloatField('Avaliação Média', default=0.0)

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'

    def aceitar_servico(self, servico):
        servico.tecnico = self
        servico.status = 'Aceito'
        servico.save()

    def atualizar_status_servico(self, servico, novo_status):
        servico.status = novo_status
        servico.save()

    def editar_perfil(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    def avaliar_cliente(self, cliente, nota, comentario=''):

        print(f'Técnico {self.nome} avaliou cliente {cliente.nome} com nota {nota}. Comentário: {comentario}')