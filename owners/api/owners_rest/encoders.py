from common.json import ModelEncoder
from .models import (
    EateryTagVO,
    EateryCategoryVO,
    EateryImageVO,
    EateryVO,
)


class EateryTagVOEncoder(ModelEncoder):
    model = EateryTagVO
    properties = ["import_href", "tag_name"]

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery.eatery_name,
                "eatery_import_href": o.eatery.import_href,
            }
        }


class EateryCategoryVOEncoder(ModelEncoder):
    model = EateryCategoryVO
    properties = ["import_href", "alias", "title"]

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery.eatery_name,
                "eatery_import_href": o.eatery.import_href,
            }
        }


class EateryImageVOEncoder(ModelEncoder):
    model = EateryImageVO
    properties = ["import_href", "image_url"]

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery.eatery_name,
                "eatery_import_href": o.eatery.import_href,
            }
        }


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
