from django.urls import path

from .api_views import (
    get_eatery_entity_data,
)

urlpatterns = [
    path("eateriesvo/", get_eatery_entity_data, name="api_get_eatery_entity_data"),
]
