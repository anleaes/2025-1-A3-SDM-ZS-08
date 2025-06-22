from django.db import models

# Create your models here.
class Pagamento(models.Model):
    METODO_CHOICES = [
        ('Pix', 'Pix'),
        ('Cartão', 'Cartão'),
        ('Dinheiro', 'Dinheiro'),
    ]
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Pago', 'Pago'),
        ('Cancelado', 'Cancelado'),
    ]

    servico = models.OneToOneField(Servico, on_delete=models.CASCADE, related_name='pagamento')
    valor = models.FloatField()
    metodo = models.CharField(max_length=10, choices=METODO_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    data = models.DateTimeField(default=timezone.now)

    def processar_pagamento(self):
        print(f'Pagamento de R${self.valor} processado via {self.metodo}.')

    def confirmar_pagamento(self):
        self.status = 'Pago'
        self.save()
        print('Pagamento confirmado.')