from django.db import models
from usuario.models import Usuario

class Cliente(Usuario):
    endereco = models.CharField('Endereço', max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def cadastrar(self):
        print(f'Cliente {self.nome} cadastrado com sucesso.')

    def editar_perfil(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        print(f'Perfil do cliente {self.nome} atualizado.')

    def solicitar_servico(self, servico):
        print(f'{self.nome} solicitou o serviço: {servico}')

    def avaliar_tecnico(self, tecnico, nota, comentario=''):
        print(f'{self.nome} avaliou o técnico {tecnico} com nota {nota}. Comentário: {comentario}')
