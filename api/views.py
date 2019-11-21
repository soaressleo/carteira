from django.shortcuts import render
from rest_framework_mongoengine import viewsets
from . import models
from . import serializers


# Create your views here.

class AtivosViewset(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = serializers.AtivosSerializer
    my_filter_fields = ('Company', 'Stock',)

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:  # iterate over the filter fields
            field_value = self.request.query_params.get(field)  # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = models.Ativos.objects.all()
        filtering_kwargs = self.get_kwargs_for_filtering()  # get the fields with values for filtering
        if filtering_kwargs:
            queryset = models.Ativos.objects.filter(**filtering_kwargs)  # filter the queryset based on 'filtering_kwargs'
        return queryset


class AtualViewset(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = models.Atual.objects.all()
    serializer_class = serializers.AtualSerializer
    my_filter_fields = ('stock', 'open', 'high', 'low', 'close', 'volume', 'date')

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:  # iterate over the filter fields
            field_value = self.request.query_params.get(field)  # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = models.Atual.objects.all()
        filtering_kwargs = self.get_kwargs_for_filtering()  # get the fields with values for filtering
        if filtering_kwargs:
            queryset = models.Atual.objects.filter(**filtering_kwargs)  # filter the queryset based on 'filtering_kwargs'
        return queryset


class HistoricoViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = models.Historico.objects.all()
    serializer_class = serializers.HistoricoSerializer
    my_filter_fields = ('stock', 'open', 'high', 'low', 'close', 'volume', 'date')

    def get_kwargs_for_filtering(self):
        filtering_kwargs = {}
        for field in self.my_filter_fields:  # iterate over the filter fields
            field_value = self.request.query_params.get(field)  # get the value of a field from request query parameter
            if field_value:
                filtering_kwargs[field] = field_value
        return filtering_kwargs

    def get_queryset(self):
        queryset = models.Historico.objects.all()
        filtering_kwargs = self.get_kwargs_for_filtering()  # get the fields with values for filtering
        if filtering_kwargs:
            queryset = models.Historico.objects.filter(**filtering_kwargs)  # filter the queryset based on 'filtering_kwargs'
        return queryset