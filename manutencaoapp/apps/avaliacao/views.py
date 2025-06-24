from .models import Avaliacao
from rest_framework import viewsets
from .serializer import AvaliacaoSerializer
from django.shortcuts import render

# Create your views here.

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer  