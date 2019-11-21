from django.db import models
from mongoengine import Document, EmbeddedDocument, fields


# Create your models here.

class Ativos(Document):
    Company = fields.StringField()
    Stock = fields.StringField()


class Atual(Document):
    stock = fields.StringField()
    open = fields.DecimalField()
    high = fields.DecimalField()
    low = fields.DecimalField()
    close = fields.DecimalField()
    volume = fields.DecimalField()
    date = fields.StringField()


class Historico(Document):
    stock = fields.StringField()
    open = fields.DecimalField()
    high = fields.DecimalField()
    low = fields.DecimalField()
    close = fields.DecimalField()
    volume = fields.DecimalField()
    date = fields.StringField()
