from .models import Eatery, EateryCategory, EateryLocation
from common.json import ModelEncoder


class EateryLocationEncoder(ModelEncoder):
    model = EateryLocation
    properties = [
        "address1",
        "address2",
        "address3",
        "city",
        "state",
        "zip",
        "country"
    ]

class EateryCategoryEncoder(ModelEncoder):
    model = EateryCategory
    props = []
    properties = [
        "alias",
        "title"
    ]

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
        "categories",
        "location"
    ]
    encoders = {
        "location": EateryLocationEncoder(),
        "categories": EateryCategoryEncoder(),
    }
    # def get_extra_data(self, o):
    #     cat_list = []
    #     for cat in :

    #     return {"categories": o.c}