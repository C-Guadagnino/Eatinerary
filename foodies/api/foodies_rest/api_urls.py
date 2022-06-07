from django.urls import path

from .api_views import (
    api_list_foodies,
)

urlpatterns = [
    path("foodies/", api_list_foodies, name="api_list_foodies"),
]
