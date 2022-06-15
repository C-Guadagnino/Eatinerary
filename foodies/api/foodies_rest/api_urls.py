from django.urls import path

from .api_views import (
    api_list_foodies,
    api_list_eateries_vo,
    api_list_tags_vo,
    api_get_specific_tag_vo,
    api_list_create_skewered_eatery,
    api_get_details_of_skewered_eatery,
    api_delete_update_skewered_eatery,
    api_list_create_review,
    api_list_create_review_images,
    api_get_details_of_review,
    api_delete_update_review,
    api_get_specific_review_image,
    api_delete_review_image,
    api_list_eatery_categories_vo,
    api_get_specific_category_vo,
)

urlpatterns = [
    path("foodies/", api_list_foodies, name="api_list_foodies"),
    path("foodies/eateries/", api_list_eateries_vo, name="api_list_eateries_vo"),
    path("foodies/tags/", api_list_tags_vo, name="api_list_tags_vo"),
    path("foodies/tags/<str:tag_name>/", api_get_specific_tag_vo, name="api_get_specific_tag_vo"),
    path("mySkewered/", api_list_create_skewered_eatery, name="api_list__create_skewered_eatery"),
    path("mySkewered/<int:pk>/", api_get_details_of_skewered_eatery, name="api_get_details_of_skewered_eatery"),
    path("mySkewered/modify/<int:pk>/", api_delete_update_skewered_eatery, name="api_delete_update_skewered_eatery"),
    path("reviews/images/", api_list_create_review_images, name="api_list_all_review_images"),
    path("reviews/images/<int:pk>/", api_get_specific_review_image, name="api_get_specific_review_image"),
    path("reviews/images/modify/<int:pk>/", api_delete_review_image, name="api_delete_review_image"),
    path("reviews/", api_list_create_review, name="api_list_create_review"),
    path("reviews/<int:pk>/", api_get_details_of_review, name="api_get_details_of_review"),
    path("reviews/modify/<int:pk>/", api_delete_update_review, name="api_delete_update_review"),
    path("categories/", api_list_eatery_categories_vo, name="api_list_eatery_categories_vo"),
    path("categories/<str:alias>/", api_get_specific_category_vo, name="api_get_specific_category_vo")
]
