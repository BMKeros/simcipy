from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Unit, Product, UnitType, Order
from .serializers import UnitSerializer, ProductSerializer, UnitTypeSerializer, OrderSerializer


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

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
