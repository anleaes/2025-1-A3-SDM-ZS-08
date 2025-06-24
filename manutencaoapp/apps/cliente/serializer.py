
from .models import Cliente # Importe a classe do modelo Cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente # CORRETO: Referencie a classe do modelo
        fields = '__all__'