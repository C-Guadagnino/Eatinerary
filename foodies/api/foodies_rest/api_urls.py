from django.urls import path

from .api_views import (
    api_foodies,
    api_eateries_vo,
    api_eatery_vo,
    api_tags_vo,
    api_tag_vo,
    api_skewered_eateries,
    api_skewered_eatery,
    api_reviews,
    api_review,
    api_review_images,
    api_review_image,
    api_categories_vo,
    api_category_vo,
    api_eatery_images_vo,
    api_eatery_image_vo,
    api_eatery_openhours_plural_vo,
    api_eatery_openhours_singular_vo,
    # NEED TO WRITE API_EATERY_OPEN_HOURS_VO
)

urlpatterns = [
    path("foodies/", api_foodies, name="api_foodies"),
    path("foodies/eateries/", api_eateries_vo, name="api_eateries_vo"),
    path(
        "foodies/eateries/<int:eatery_entity_id>/",
        api_eatery_vo,
        name="api_eatery_vo",
    ),
    path("foodies/eateries/tags/", api_tags_vo, name="api_tags_vo"),
    path(
        "foodies/eateries/tags/<str:tag_name>/",
        api_tag_vo,
        name="api_tag_vo",
    ),
    path(
        "skewered/",
        api_skewered_eateries,
        name="api_skewered_eateries",
    ),
    path(
        "skewered/<int:pk>/",
        api_skewered_eatery,
        name="api_skewered_eatery",
    ),
    path(
        "reviews/images/",
        api_review_images,
        name="api_review_images",
    ),
    path(
        "reviews/images/<int:pk>/",
        api_review_image,
        name="api_review_image",
    ),
    path("eateries/reviews/", api_reviews, name="api_reviews"),
    path("eateries/reviews/<int:pk>/", api_review, name="api_review"),
    path(
        "categories/",
        api_categories_vo,
        name="api_categories_vo",
    ),
    path(
        "categories/<str:alias>/",
        api_category_vo,
        name="api_category_vo",
    ),
    path("eateries/images/", api_eatery_images_vo, name="api_eatery_images_vo"),
    path(
        "eateries/images/<int:eatery_image_entity_id>/",
        api_eatery_image_vo,
        name="api_eatery_image_vo",
    ),
    path(
        "eateries/openhours/",
        api_eatery_openhours_plural_vo,
        name="api_eatery_openhours_plural_vo",
    ),
    path(
        "eateries/openhours/<int:eatery_openhours_entity_id>/",
        api_eatery_openhours_singular_vo,
        name="api_eatery_openhours_singular_vo",
    ),
]
