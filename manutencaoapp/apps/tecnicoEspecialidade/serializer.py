from .models import TecnicoEspecialidade

from rest_framework import serializers

class TecnicoEspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = "Tecnico Especialidade"
        fields = '__all__'