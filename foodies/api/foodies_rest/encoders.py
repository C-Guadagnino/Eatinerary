from common.json import ModelEncoder
from .resources import STATES
from .models import (
    EateryTagVO, 
    EateryCategoriesVO, 
    EateryLocationVO, 
    ImageVO, 
    Foodie, 
    EateryVO, 
    SkeweredEatery, 
    Review)

class EateryTagVOEncoder(ModelEncoder):
    model = EateryTagVO
    properties = ["tag_name"]

class EateryCategoriesVOEncoder(ModelEncoder):
    model = EateryCategoriesVO
    properties = ["alias", "title"]

class EateryLocationVOEncoder(ModelEncoder):
    model = EateryLocationVO
    properties = [
        "address1",
        "address2",
        "address3",
        "city",
        "state",
        "zip",
        "country"
    ]
    #needs review
    def get_extra_data(self,o):
        return {"states": STATES}

class ImageVOEncoder(ModelEncoder):
    model = ImageVO
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
        "price"
        "eatery_open_hours",
        "location",
        "tag",
        "categories"
    ]
    encoders = {
        "location": EateryLocationVOEncoder(),
        "tag": EateryTagVOEncoder(),
        "categories": EateryCategoriesVOEncoder(),
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
        "notes"
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
        "image"
    ]
    encoders = {
        "skewered_restaurant": SkeweredEateryEncoder(),
        "image": ImageVOEncoder()
    }