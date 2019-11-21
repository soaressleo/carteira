from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


# Create your views here.

class AtivosViewset(viewsets.ModelViewSet):
    queryset = models.Ativos.objects.all()
    serializer_class = serializers.AtivosSerializer
    filterset_fields = ('Company', 'Stock',)


class AtualViewset(viewsets.ModelViewSet):
    queryset = models.Atual.objects.all()
    serializer_class = serializers.AtualSerializer
    filterset_fields = ('stock', 'open', 'high', 'low', 'close', 'volume', 'date')


class HistoricoViewSet(viewsets.ModelViewSet):
    queryset = models.Historico.objects.all()
    serializer_class = serializers.HistoricoSerializer
    filterset_fields = ('stock', 'open', 'high', 'low', 'close', 'volume', 'date')