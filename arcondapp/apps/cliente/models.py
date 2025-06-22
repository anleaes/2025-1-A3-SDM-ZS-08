from django.db import models
from usuario.models import Usuario
# Importe Tecnico do seu próprio aplicativo 'tecnico' se for necessário
# Se a classe Cliente usar Tecnico, descomente a linha abaixo:
# from tecnico.models import Tecnico

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
        # Se Tecnico for importado acima, este método funcionará
        print(f'{self.nome} avaliou o técnico {tecnico} com nota {nota}. Comentário: {comentario}')