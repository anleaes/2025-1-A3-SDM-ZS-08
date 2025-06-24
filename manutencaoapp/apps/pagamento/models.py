from django.db import models
from django.utils import timezone

class Pagamento(models.Model):
    FORMA_PAGAMENTO_CHOICES = [
        ('pix', 'PIX'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('boleto', 'Boleto'),
        ('dinheiro', 'Dinheiro'),
    ]

    STATUS_PAGAMENTO_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
        ('estornado', 'Estornado'),
    ]

    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE, related_name='pagamentos')
    servico = models.ForeignKey('servico.Servico', on_delete=models.CASCADE, related_name='pagamentos')
    
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_PAGAMENTO_CHOICES, default='pendente')
    data_pagamento = models.DateTimeField(default=timezone.now)

    comprovante = models.ImageField(upload_to='comprovantes/', null=True, blank=True)

    def __str__(self):
        return f"Pagamento de R$ {self.valor} - {self.status}"
