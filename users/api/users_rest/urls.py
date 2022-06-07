from django.urls import path

from .views import api_users, api_user_token

urlpatterns = [
    path("users/", api_users, name="api_users"),
    path("users/me/token/", api_user_token, name="api_user_token"),
]
