from django.db import models
from django.contrib.auth.models import User


class UnitType(models.Model):
    name = models.CharField(max_length=80)


class Unit(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=8)
    type = models.ForeignKey(UnitType, on_delete=None)


class Warehouse(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    responsible = models.ForeignKey(User, on_delete=None)
