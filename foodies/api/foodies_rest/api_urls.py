from django.urls import path

from .views import(
    api_list_foodies,
    api_get_yelp,
)

urlpatterns = [
    path("foodies/", api_list_foodies, name="api_list_foodies"),
    path("yelp/", api_get_yelp, name="api_get_yelp"),
]