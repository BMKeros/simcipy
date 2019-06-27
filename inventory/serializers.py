from rest_framework import serializers
from .models import Unit, UnitType, Product


class UnitTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80)

    def create(self, validated_data):
        return UnitType.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance


class UnitSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    abbreviation = serializers.CharField(max_length=8)
    type = serializers.PrimaryKeyRelatedField(queryset=UnitType.objects.all())

    def create(self, validated_data):
        return Unit.objects.create(**validated_data)


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=300)
    specs = serializers.CharField(max_length=300)
    unit = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all())

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
