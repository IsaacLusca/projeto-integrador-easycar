from rest_framework import serializers
from .models import Carro

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['modelo', 'placa', 'ano', 'valor_diaria', 'status']
        read_only_fields = ['status']  # impede alterar direto
