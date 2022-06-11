from django.urls import path

from .api_views import (
    api_eateries,
    api_eatery,
    api_category,
    api_location,
    api_locations,
    api_tags,
    api_categories,
    api_open_hours_plural,
    api_open_hours_singular,
    api_eatery_images,
    api_eatery_image,
    api_return_list_of_restaurants_given_category_and_location,
    # api_get_yelp_with_category_and_location,
    api_get_yelp_with_location,
    api_tag,
    api_get_yelp_one_eatery,
    api_yelp_location_search_terms,
    api_yelp_category_search_terms,
    api_yelp_result
)

urlpatterns = [
    path(
        "yelp/<str:location>/",
        api_get_yelp_with_location,
        name="api_get_yelp_with_location",
    ),
    path(
        "yelpresults/",
        api_yelp_result,
        name="api_yelp_result",
    ),
    path(
        "locationsearchterms/",
        api_yelp_location_search_terms,
        name="api_yelp_location_search_terms",
    ),
    path(
        "categorysearchterms/",
        api_yelp_category_search_terms,
        name="api_yelp_category_search_terms",
    ),
    path(
        "yelp/one/<str:yelp_id>/",
        api_get_yelp_one_eatery,
        name="api_get_yelp_one_eatery",
    ),
    path(
        "yelp/<str:location>/<str:category>/",
        api_return_list_of_restaurants_given_category_and_location,
        name="api_return_list_of_restaurants_given_category_and_location",
    ),
    path("eateries/", api_eateries, name="api_eateries"),
    path("eateries/<int:pk>/", api_eatery, name="api_eatery"),
    path("locations/", api_locations, name="api_locations"),
    path("locations/<int:pk>/", api_location, name="api_location"),
    path("category/<int:pk>/", api_category, name="api_category"),
    path("tags/", api_tags, name="api_tags"),
    path("tags/<int:pk>/", api_tag, name="api_tag"),
    path("categories/", api_categories, name="api_categories"),
    path("openhours/", api_open_hours_plural, name="api_open_hours_plural"),
    path(
        "openhours/<int:pk>/", api_open_hours_singular, name="api_open_hours_singular"
    ),
    path("eateryimages/", api_eatery_images, name="api_eatery_images"),
    path("eateryimages/<int:pk>/", api_eatery_image, name="api_eatery_image"),
]
