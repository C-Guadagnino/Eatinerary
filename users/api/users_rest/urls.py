from django.urls import path

from .views import api_users, api_user_token, api_get_specific_user, api_list_users

urlpatterns = [
    path("users/", api_users, name="api_users"),
    path("users/<int:pk>/", api_get_specific_user, name="api_users"),
    path("users/all/", api_list_users, name="api_list_users"),
    path("users/me/token/", api_user_token, name="api_user_token"),
]
