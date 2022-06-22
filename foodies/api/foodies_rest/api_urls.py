from django.urls import path

from .api_views import (
    api_foodies,
    api_foodie,
    api_eateries_vo,
    api_eatery_vo,
    api_categories_vo,
    api_category_vo,
    api_tags_vo,
    api_tag_vo,
    api_eatery_openhours_plural_vo,
    api_eatery_openhours_singular_vo,
    api_eatery_images_vo,
    api_eatery_image_vo,
    api_skewered_eateries,
    api_skewered_eatery,
    api_reviews,
    api_review,
    api_review_images,
    api_review_image,
    api_special_dates,
    api_special_date,
    api_show_skeweredeateries_for_specific_foodie,
)

urlpatterns = [
    path("foodies/", api_foodies, name="api_foodies"),
    path("foodies/<str:username>/", api_foodie, name="api_foodie"),
    path("foodies/eateries/", api_eateries_vo, name="api_eateries_vo"),
    path(
        "foodies/eateries/<int:eatery_entity_id>/", api_eatery_vo, name="api_eatery_vo"
    ),
    path("foodies/eateries/categories/", api_categories_vo, name="api_categories_vo"),
    path(
        "foodies/eateries/categories/<str:alias>/",
        api_category_vo,
        name="api_category_vo",
    ),
    path("foodies/eateries/tags/", api_tags_vo, name="api_tags_vo"),
    path("foodies/eateries/tags/<str:tag_name>/", api_tag_vo, name="api_tag_vo"),
    path(
        "foodies/eateries/openhours/",
        api_eatery_openhours_plural_vo,
        name="api_eatery_openhours_plural_vo",
    ),
    path(
        "foodies/eateries/openhours/<int:eatery_openhours_entity_id>/",
        api_eatery_openhours_singular_vo,
        name="api_eatery_openhours_singular_vo",
    ),
    path("foodies/eateries/images/", api_eatery_images_vo, name="api_eatery_images_vo"),
    path(
        "foodies/eateries/images/<int:eatery_image_entity_id>/",
        api_eatery_image_vo,
        name="api_eatery_image_vo",
    ),
    path(
        "foodies/eateries/skewered/",
        api_skewered_eateries,
        name="api_skewered_eateries",
    ),
    path(
        "foodies/eateries/skewered/<int:pk>/",
        api_skewered_eatery,
        name="api_skewered_eatery",
    ),
    path("foodies/eateries/reviews/", api_reviews, name="api_reviews"),
    path("foodies/eateries/reviews/<int:pk>/", api_review, name="api_review"),
    path(
        "foodies/eateries/reviews/images/", api_review_images, name="api_review_images"
    ),
    path(
        "foodies/eateries/reviews/images/<int:pk>/",
        api_review_image,
        name="api_review_image",
    ),
    path("foodies/specialdates/", api_special_dates, name="api_special_dates"),
    path(
        "foodies/<int:foodie_id>/specialdates/",
        api_special_dates,
        name="api_special_dates_for_foodie",
    ),
    path("foodies/specialdates/<int:pk>/", api_special_date, name="api_special_date"),
    path(
        "foodies/eateries/skeweredtest/<str:username>/",
        api_show_skeweredeateries_for_specific_foodie,
        name="api_skewered_eatery_for_user",
    ),
]
