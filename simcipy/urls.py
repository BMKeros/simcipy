from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('api/', include('core.urls')),
    path('api/', include('inventory.urls'))
]
