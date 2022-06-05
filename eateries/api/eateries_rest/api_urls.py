from django.urls import path

from .api_views import (
    api_get_eatery_data,
    api_get_yelp 
)

urlpatterns = [
    path("yelp/", api_get_yelp, name="api_get_yelp"),
    path("eateries/", api_get_eatery_data, name="api_get_eatery_data"),
]