from django.urls import path

from .api_views import (
    api_eateries,
    api_eateries_given_category_and_location,
    api_eatery,
    api_locations,
    api_location,
    api_categories,
    api_category,
    api_tags,
    api_tag,
    api_open_hours_plural,
    api_open_hours_singular,
    api_eatery_images,
    api_eatery_image,
    # api_get_yelp_with_location,
    api_location_search_terms,
    api_category_search_terms,
    api_yelp_results,
    # api_filtered_eateries
    # api_get_yelp_one_eatery,
    # api_get_yelp_with_category_and_location,
    # api_yelp_results_from_db
)

urlpatterns = [
    path("eateries/", api_eateries, name="api_eateries"),
    path(
        "eateries/yelp/<str:location>/<str:category>/",
        api_eateries_given_category_and_location,
        name="api_eateries_given_category_and_location",
    ),
    path("eateries/<int:pk>/", api_eatery, name="api_eatery"),
    path("eateries/locations/", api_locations, name="api_locations"),
    path("eateries/locations/<int:pk>/", api_location, name="api_location"),
    path("eateries/categories/", api_categories, name="api_categories"),
    path("eateries/category/<int:pk>/", api_category, name="api_category"),
    path("eateries/tags/", api_tags, name="api_tags"),
    path("eateries/tags/<str:tag_name>/", api_tag, name="api_tag"),
    path("eateries/openhours/", api_open_hours_plural, name="api_open_hours_plural"),
    path(
        "eateries/openhours/<int:pk>/",
        api_open_hours_singular,
        name="api_open_hours_singular",
    ),
    path("eateries/eateryimages/", api_eatery_images, name="api_eatery_images"),
    path("eateries/eateryimages/<int:pk>/", api_eatery_image, name="api_eatery_image"),
    path(
        "eateries/locationsearchterms/",
        api_location_search_terms,
        name="api_location_search_terms",
    ),
    path(
        "eateries/categorysearchterms/",
        api_category_search_terms,
        name="api_category_search_terms",
    ),
    path(
        "eateries/yelpresults/",
        api_yelp_results,
        name="api_yelp_results",
    ),
    # path(
    #     "eateries/<str:city>/<str:alias>/",
    #     api_filtered_eateries,
    #     name="api_filtered_eateries",
    # ),
    # path(
    #     "eateries/yelp/<str:location>/",
    #     api_get_yelp_with_location,
    #     name="api_get_yelp_with_location",
    # ),
    # path(
    #     "yelpdb/<str:location>/<str:category>/",
    #     api_yelp_results_from_db,
    #     name="api_yelp_results_from_db",
    # ),
    # path(
    #     "yelp/one/<str:yelp_id>/",
    #     api_get_yelp_one_eatery,
    #     name="api_get_yelp_one_eatery",
    # ),
]
