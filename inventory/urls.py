from django.urls import path, include
from .views import UnitViewSet, ProductViewSet, UnitTypeWiewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'unit-types', UnitTypeWiewSet)
router.register(r'units', UnitViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
