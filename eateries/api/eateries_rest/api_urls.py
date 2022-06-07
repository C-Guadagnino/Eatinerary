from django.urls import path

from .api_views import (
    api_eateries,
    api_get_yelp,
    api_eatery,
    api_category,
    api_location,
    api_locations,
)

urlpatterns = [
    path("yelp/", api_get_yelp, name="api_get_yelp"),
    path("eateries/", api_eateries, name="api_eateries"),
    path("eateries/<int:pk>/", api_eatery, name="api_eatery"),
    path("locations/", api_locations, name="api_locations"),
    path("locations/<int:pk>/", api_location, name="api_location"),
    path("category/<int:pk>/", api_category, name="api_category"),
]
