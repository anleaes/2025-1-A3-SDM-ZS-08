from django.shortcuts import render
from .models import Tecnico
from rest_framework import viewsets
from .serializer import TecnicoSerializer

# Create your views here.

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer  