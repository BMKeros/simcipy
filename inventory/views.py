from rest_framework.viewsets import ModelViewSet
from .models import Unit
from .serializers import UnitSerializer


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
