from django.urls import path

from .api_views import (
    api_get_eatery_data,
    api_get_yelp,
    api_get_eatery,
    api_get_category,
    api_get_location
)

urlpatterns = [
    path("yelp/", api_get_yelp, name="api_get_yelp"),
    path("eateries/", api_get_eatery_data, name="api_get_eatery_data"),
    path("eatery/<int:pk>/", api_get_eatery, name="api_get_eatery"),
    path("location/<int:pk>/", api_get_location, name="api_get_location"),
    path("category/<int:pk>/", api_get_category, name="api_get_category")
]