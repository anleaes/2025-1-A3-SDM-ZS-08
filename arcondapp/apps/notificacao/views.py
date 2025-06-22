from django.shortcuts import render
from .models import Notificacao
from rest_framework import viewsets
from .serializer import NotificacaoSerializer

# Create your views here.
class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer  