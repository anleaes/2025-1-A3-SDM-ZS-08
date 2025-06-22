from django.shortcuts import render
from .models import Endereco
from rest_framework import viewsets
from .serializer import EnderecoSerializer

# Create your views here.
class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer  