from .models import TecnicoEspecialidade
from rest_framework import serializers

class TecnicoEspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicoEspecialidade
        fields = '__all__'
