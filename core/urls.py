from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from .views import UserDetail, UserList

urlpatterns = [
    path('token/create/', obtain_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('token/verify/', verify_jwt_token),

    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view())
]
