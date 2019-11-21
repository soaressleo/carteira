from rest_framework import serializers
from . import models


class AtivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ativos
        fields = '__all__'


class AtualSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Atual
        fields = '__all__'


class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Historico
        fields = '__all__'
