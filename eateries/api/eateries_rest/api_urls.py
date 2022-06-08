from django.urls import path

from .api_views import (
    api_eateries,
    api_get_yelp,
    api_eatery,
    api_category,
    api_location,
    api_locations,
    api_tags,
    api_categories,
    api_open_hours_plural,
    api_open_hours_singular,
    api_eatery_images,
    api_eatery_image
)

urlpatterns = [
    path("yelp/", api_get_yelp, name="api_get_yelp"),
    path("eateries/", api_eateries, name="api_eateries"),
    path("eateries/<int:pk>/", api_eatery, name="api_eatery"),
    path("locations/", api_locations, name="api_locations"),
    path("locations/<int:pk>/", api_location, name="api_location"),
    path("category/<int:pk>/", api_category, name="api_category"),
    path("tags/", api_tags, name="api_tags"),
    path("categories/", api_categories, name="api_categories"),
    path("openhours/", api_open_hours_plural, name="api_open_hours_plural"),
    path("openhours/<int:pk>/", api_open_hours_singular, name="api_open_hours_singular"),
    path("eateryimages/", api_eatery_images, name="api_eatery_images"),
    path("eateryimages/<int:pk>/", api_eatery_image, name="api_eatery_image"),
]
