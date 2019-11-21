from django.db import models


# Create your models here.

class Ativos(models.Model):

    Company = models.CharField(max_length=250)
    Stock = models.CharField(max_length=20)


class Atual(models.Model):

    stock = models.CharField(max_length=20)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.CharField(max_length=20)

class Historico(models.Model):
    stock = models.CharField(max_length=20)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.CharField(max_length=20)
