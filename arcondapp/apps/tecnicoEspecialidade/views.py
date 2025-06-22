from django.shortcuts import render
from .models import TecnicoEspecialidade
from rest_framework import viewsets
from .serializer import TecnicoEspecialideSerializer

# Create your views here.

class TecnicoEspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = TecnicoEspecialidade.objects.all()
    serializer_class = TecnicoEspecialideSerializer 