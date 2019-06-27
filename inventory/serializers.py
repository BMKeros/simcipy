from rest_framework import serializers


class UnitSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    abbreviation = serializers.CharField(max_length=8)
