from django.urls import path
from .views import UnitViewSet

urlpatterns = [
    path('units/', UnitViewSet),
]
