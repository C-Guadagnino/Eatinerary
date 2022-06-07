from django.urls import path

from .api_views import (
    get_eatery_entity_data,
    api_get_eateryvo
)

urlpatterns = [
    path("eateriesvo/", get_eatery_entity_data, name="api_get_eatery_entity_data"),
    path("eateriesvo/<str:email>/", api_get_eateryvo, name="api_get_eateryvo")
]
