from django.db import models


class UnitType(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)
    type = models.ForeignKey(UnitType, on_delete=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    specs = models.TextField(max_length=300)
    unit = models.ForeignKey(Unit, on_delete=None)

    def __str__(self):
        return self.name
