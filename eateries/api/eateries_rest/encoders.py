from .models import (
    Eatery,
    EateryCategory,
    EateryLocation,
    Tag,
    EateryOpenHours,
    EateryImage,
    WEEKDAYS,
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
        "zip",
        "country",
    ]


class EateryCategoryEncoder(ModelEncoder):
    model = EateryCategory
    props = []
    properties = ["id", "alias", "title"]


class TagEncoder(ModelEncoder):
    model = Tag
    properties = ["id", "tag_name"]


class OpenHoursEncoder(ModelEncoder):
    model = EateryOpenHours
    properties = ["id", "start_time", "end_time"]

    def get_extra_data(self, o):
        return {
            "weekday": WEEKDAYS[o.weekday - 1][1],
            "eatery": {"eatery_name": o.eatery.eatery_name, "eatery_id": o.eatery.id},
        }


class EateryImageEncoder(ModelEncoder):
    model = EateryImage
    properties = ["id", "image_url"]

    def get_extra_data(self, o):
        return {
            "eatery": {"eatery_name": o.eatery.eatery_name, "eatery_id": o.eatery.id}
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
    ]
    encoders = {
        "location": EateryLocationEncoder(),
        "categories": EateryCategoryEncoder(),
        "tags": TagEncoder(),
        "open_hours": OpenHoursEncoder(),
        "eatery_images": EateryImageEncoder(),
    }
