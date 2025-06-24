from .models import Servico
from rest_framework import viewsets
from .serializer import ServicoSerializer
from django.shortcuts import render

# Create your views here.

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer  