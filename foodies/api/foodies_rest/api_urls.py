from django.urls import path

from .api_views import (
    api_list_foodies,
    api_list_eateries,
    api_list_skewered_eateries
)

urlpatterns = [
    path("foodies/", api_list_foodies, name="api_list_foodies"),
    path("foodies/eateries/", api_list_eateries, name="api_list_eateries"),
    path("mySkewered/", api_list_skewered_eateries, name="api_list_skewered_eateries"),
]
