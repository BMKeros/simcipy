from django.db import models


class UnitType(models.Model):
    name = models.CharField(max_length=80)


class Unit(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)
    type = models.ForeignKey(UnitType, on_delete=None)

class Product(models.Model):
    pass