from .models import TecnicoEspecialidade
from .models import Especialidade
from rest_framework import viewsets
from .serializer import TecnicoEspecialidadeSerializer
from .serializer import EspecialidadeSerializer
from django.shortcuts import render

# Create your views here.

class TecnicoEspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = TecnicoEspecialidade.objects.all()
    serializer_class = TecnicoEspecialidadeSerializer  

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = TecnicoEspecialidade.objects.all()
    serializer_class = EspecialidadeSerializer  