from django.shortcuts import render
from .models import Avaliacao
from rest_framework import viewsets
from .serializer import AvaliacaoSerializer

# Create your views here.
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer  