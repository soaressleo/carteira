from rest_framework_mongoengine import serializers
from . import models


class AtivosSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Ativos
        fields = '__all__'


class AtualSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Atual
        fields = '__all__'


class HistoricoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Historico
        fields = '__all__'
