from django.db import models
from django.contrib.auth.models import User


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


class Warehouse(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    responsible = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    specs = models.TextField(max_length=300)
    unit = models.ForeignKey(Unit, on_delete=None)

    def __str__(self):
        return self.name
