from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Unit, Product, UnitType
from .serializers import UnitSerializer, ProductSerializer, UnitTypeSerializer


class UnitTypeWiewSet(ModelViewSet):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
