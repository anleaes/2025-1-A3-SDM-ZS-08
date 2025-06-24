from .models import Pagamento
from rest_framework import viewsets
from .serializer import PagamentoSerializer
from django.shortcuts import render

# Create your views here.

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer  