from .models import Notificacao
from rest_framework import serializers

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'
