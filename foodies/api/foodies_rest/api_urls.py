from django.urls import path

from .api_views import (
    api_list_foodies,
    api_list_eateries_vo,
    api_list_tags_vo,
    api_get_specific_tag_vo,
    api_list_create_skewered_eatery,
    api_get_details_of_skewered_eatery,
    api_delete_update_skewered_eatery,
    api_list_create_reviews,
    api_list_create_review_images,
    api_get_details_of_review,
    api_delete_update_review,
    api_get_details_of_review_based_on_skeweredeatery,
    api_get_specific_review_image,
    api_delete_review_image,
    api_list_eatery_categories_vo,
    api_get_specific_category_vo,
    api_list_eatery_images_vo,
    api_get_specific_eatery_image_vo,
)

urlpatterns = [
    path("foodies/", api_list_foodies, name="api_list_foodies"),
    path("foodies/eateries/", api_list_eateries_vo, name="api_list_eateries_vo"),
    path("foodies/tags/", api_list_tags_vo, name="api_list_tags_vo"),
    path(
        "foodies/tags/<str:tag_name>/",
        api_get_specific_tag_vo,
        name="api_get_specific_tag_vo",
    ),
    path(
        "mySkewered/",
        api_list_create_skewered_eatery,
        name="api_list__create_skewered_eatery",
    ),
    path(
        "mySkewered/<int:pk>/",
        api_get_details_of_skewered_eatery,
        name="api_get_details_of_skewered_eatery",
    ),
    path(
        "mySkewered/modify/<int:pk>/",
        api_delete_update_skewered_eatery,
        name="api_delete_update_skewered_eatery",
    ),
    # path("reviews/images/", api_list_create_review_images, name="api_list_create_review_images"),
    path(
        "reviews/<int:review_id>/images/",
        api_list_create_review_images,
        name="api_list_create_review_images",
    ),
    path(
        "reviews/images/",
        api_list_create_review_images,
        name="api_list_create_review_images",
    ),
    path(
        "reviews/images/<int:pk>/",
        api_get_specific_review_image,
        name="api_get_specific_review_image",
    ),
    path(
        "reviews/images/modify/<int:pk>/",
        api_delete_review_image,
        name="api_delete_review_image",
    ),
    path("reviews/", api_list_create_reviews, name="api_list_create_reviews"),
    path(
        "reviews/<int:eatery_entity_id>/",
        api_list_create_reviews,
        name="api_list_create_reviews_for_eatery",
    ),
    path(
        "reviews/<int:pk>/", api_get_details_of_review, name="api_get_details_of_review"
    ),
    path(
        "reviews/modify/<int:pk>/",
        api_delete_update_review,
        name="api_delete_update_review",
    ),
    path(
        "reviews/skewered/<int:skeweredeatery_id>/",
        api_get_details_of_review_based_on_skeweredeatery,
        name="api_get_details_of_review_based_on_skeweredeatery",
    ),
    path(
        "categories/",
        api_list_eatery_categories_vo,
        name="api_list_eatery_categories_vo",
    ),
    path(
        "categories/<str:alias>/",
        api_get_specific_category_vo,
        name="api_get_specific_category_vo",
    ),
    path("eateryImages/", api_list_eatery_images_vo, name="api_list_eatery_images_vo"),
    path(
        "eateryImages/<int:eatery_image_entity_id>/",
        api_get_specific_eatery_image_vo,
        name="api_get_specific_eatery_image_vo",
    ),
]
