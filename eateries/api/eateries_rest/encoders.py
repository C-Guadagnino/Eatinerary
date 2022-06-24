from .models import (
    Eatery,
    EateryCategory,
    EateryLocation,
    EateryTag,
    EateryOpenHours,
    EateryImage,
    WEEKDAYS,
    YelpLocationSearchTerm,
    YelpCategorySearchTerm,
    YelpResult,
)
from common.json import ModelEncoder


class EateryLocationEncoder(ModelEncoder):
    model = EateryLocation
    properties = [
        "id",
        "address1",
        "address2",
        "address3",
        "city",
        "state",
        "zip_code",
        "country",
    ]


class EateryCategoryEncoder(ModelEncoder):
    model = EateryCategory
    properties = ["id", "alias", "title"]


class EateryTagEncoder(ModelEncoder):
    model = EateryTag
    properties = ["id", "tag_name"]


class YelpLocationSearchTermEncoder(ModelEncoder):
    model = YelpLocationSearchTerm
    properties = ["id", "location_term"]


class YelpCategorySearchTermEncoder(ModelEncoder):
    model = YelpCategorySearchTerm
    properties = ["id", "category_term"]


class YelpResultEncoder(ModelEncoder):
    model = YelpResult
    properties = ["id", "category_term", "location_term"]
    encoders = {
        "category_term": YelpCategorySearchTermEncoder(),
        "location_term": YelpLocationSearchTermEncoder(),
    }

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery.eatery_name,
                "eatery_id": o.eatery.id,
            },
        }


class EateryOpenHoursEncoder(ModelEncoder):
    model = EateryOpenHours
    properties = ["id", "start_time", "end_time"]

    def get_extra_data(self, o):
        return {
            "weekday": WEEKDAYS[o.weekday - 1][1],
            "eatery": {
                "eatery_name": o.eatery.eatery_name,
                "eatery_id": o.eatery.id,
            },
        }


class EateryImageEncoder(ModelEncoder):
    model = EateryImage
    properties = ["id", "image_url"]

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery.eatery_name,
                "eatery_id": o.eatery.id,
            }
        }


class EateryEncoder(ModelEncoder):
    model = Eatery
    properties = [
        "id",
        "eatery_name",
        "website",
        "email",
        "phone",
        "yelp_id",
        "review_count",
        "average_rating",
        "price",
        "from_yelp",
        "categories",
        "location",
        "tags",
        "open_hours",
        "eatery_images",
        "latitude",
        "longitude",
    ]
    encoders = {
        "location": EateryLocationEncoder(),
        "categories": EateryCategoryEncoder(),
        "tags": EateryTagEncoder(),
        "open_hours": EateryOpenHoursEncoder(),
        "eatery_images": EateryImageEncoder(),
    }
