from .models import TecnicoEspecialidade
from .models import Especialidade

from rest_framework import serializers

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = "Especialidade"
        fields = '__all__'

class TecnicoEspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = "Tecnico Especialidade"
        fields = '__all__'