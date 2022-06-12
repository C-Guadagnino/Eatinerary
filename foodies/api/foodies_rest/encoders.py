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
    properties = ["import_href", "tag_name"]

    def get_extra_data(self, o):
        return {
            "eatery": {"eatery_name": o.eatery.eatery_name, "eatery_import_href": o.eatery.import_href}
        }


class EateryCategoryVOEncoder(ModelEncoder):
    model = EateryCategoryVO
    properties = ["import_href", "alias", "title"]

    def get_extra_data(self, o):
        return {
            "eatery": {"eatery_name": o.eatery.eatery_name, "eatery_import_href": o.eatery.import_href}
        }


class EateryImageVOEncoder(ModelEncoder):
    model = EateryImageVO
    properties = ["image_url"]

    def get_extra_data(self, o):
        return {
            "eatery": {"eatery_name": o.eatery.eatery_name, "eatery_import_href": o.eatery.import_href}
        }

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
        "from_yelp",
        "location_address1",
        "location_address2",
        "location_address3",
        "location_city",
        "location_state",
        "location_zip",
        "location_country",
        "latitude",
        "longitude",

    ]

class SkeweredEateryEncoder(ModelEncoder):
    model = SkeweredEatery
    properties = [
        "id",
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
        "id",
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
