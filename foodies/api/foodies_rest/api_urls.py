from django.urls import path

from .api_views import (
    api_list_foodies,
    api_list_eateries_vo,
    api_list_tags_vo,
    api_list_create_skewered_eatery,
    api_get_details_of_skewered_eatery,
    api_delete_update_skewered_eatery,
)

urlpatterns = [
    path("foodies/", api_list_foodies, name="api_list_foodies"),
    path("foodies/eateries/", api_list_eateries_vo, name="api_list_eateries_vo"),
    path("foodies/tags/", api_list_tags_vo, name="api_list_tags_vo"),
    path("mySkewered/", api_list_create_skewered_eatery, name="api_list__create_skewered_eatery"),
    path("mySkewered/<int:pk>/", api_get_details_of_skewered_eatery, name="api_get_details_of_skewered_eatery"),
    path("mySkewered/modify/<int:pk>/", api_delete_update_skewered_eatery, name="api_delete_update_skewered_eatery"),
]
