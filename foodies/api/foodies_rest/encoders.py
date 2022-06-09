from common.json import ModelEncoder
from .models import (
    EateryTagVO,
    EateryCategoryVO,
    EateryImageVO,
    Foodie,
    EateryVO,
    SkeweredEatery,
    Review,
)


class EateryTagVOEncoder(ModelEncoder):
    model = EateryTagVO
    properties = ["tag_name", "import_href"]


class EateryCategoryVOEncoder(ModelEncoder):
    model = EateryCategoryVO
    properties = ["alias", "title"]


class EateryImageVOEncoder(ModelEncoder):
    model = EateryImageVO
    properties = ["image_url"]


class FoodieEncoder(ModelEncoder):
    model = Foodie
    properties = [
        "username",
        "first_name",
        "email",
        "phone",
        "google_calendar",
    ]


class EateryVOEncoder(ModelEncoder):
    model = EateryVO
    properties = [
        "import_href",
        "eatery_name",
        "email",
        "phone",
        "website",
        "yelp_id",
        "review_count",
        "average_rating",
        "price",
        # "eatery_open_hours",
        # "tags",
        # "categories",
        "location_address1",
        "location_address2",
        "location_address3",
        "location_city",
        "location_state",
        "location_zip",
        "location_country",
    ]
    encoders = {
        "tag": EateryTagVOEncoder(),
        "categories": EateryCategoryVOEncoder(),
    }


class SkeweredEateryEncoder(ModelEncoder):
    model = SkeweredEatery
    properties = [
        "eatery",
        "foodie",
        "created_DateTime",
        "updated_DateTime",
        "has_visited",
        "is_active",
        "notes",
    ]
    encoders = {
        "eatery": EateryVOEncoder(),
        "foodie": FoodieEncoder(),
    }


class ReviewEncoder(ModelEncoder):
    model = Review
    properties = [
        "title",
        "rating",
        "created_DateTime",
        "description",
        "skewered_restaurant",
        "image",
    ]
    encoders = {
        "skewered_restaurant": SkeweredEateryEncoder(),
        "image": EateryImageVOEncoder(),
    }
