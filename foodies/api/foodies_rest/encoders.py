from common.json import ModelEncoder
from .models import (
    EateryVO,
    EateryCategoryVO,
    EateryTagVO,
    EateryOpenHoursVO,
    EateryImageVO,
    FoodieVO,
    SkeweredEatery,
    Review,
    ReviewImage,
    SpecialDate,
)


class EateryCategoryVOEncoder(ModelEncoder):
    model = EateryCategoryVO
    properties = ["import_href", "alias", "title"]


class EateryTagVOEncoder(ModelEncoder):
    model = EateryTagVO
    properties = ["import_href", "tag_name"]


class EateryOpenHoursVOEncoder(ModelEncoder):
    model = EateryOpenHoursVO
    properties = ["import_href", "weekday", "start_time", "end_time"]


class EateryImageVOEncoder(ModelEncoder):
    model = EateryImageVO
    properties = ["import_href", "image_url"]


class SkeweredEateryEncoder(ModelEncoder):
    model = SkeweredEatery
    properties = [
        "id",
        "created_DateTime",
        "updated_DateTime",
        "has_visited",
        "is_active",
        "notes",
        # "review",
    ]
    # encoders = {"review": ReviewEncoder()}

    def get_extra_data(self, o):
        eatery_info = {
            "eatery_name": o.eatery_vo.eatery_name,
            "eatery_import_href": o.eatery_vo.import_href,
        }
        foodie_info = {
            "foodie_username": o.foodie.username,
            "foodie_firstname": o.foodie.first_name,
            "foodie_lastname": o.foodie.last_name,
        }
        return {
            "eatery": eatery_info,
            "foodie": foodie_info,
        }


class ReviewImageEncoder(ModelEncoder):
    model = ReviewImage
    properties = ["id", "image_url"]


class ReviewEncoder(ModelEncoder):
    model = Review
    properties = [
        "id",
        "title",
        "rating",
        "created_DateTime",
        "description",
        "review_images",
        "skewered_eatery",
    ]
    encoders = {
        "review_images": ReviewImageEncoder(),
        "skewered_eatery": SkeweredEateryEncoder(),
    }


class FoodieEncoder(ModelEncoder):
    model = FoodieVO
    properties = [
        "username",
        "first_name",
        "email",
        "phone",
        # "google_calendar",
        "skewered_eateries",
    ]
    encoders = {"skewered_eateries": SkeweredEateryEncoder()}


class SpecialDateEncoder(ModelEncoder):
    model = SpecialDate
    properties = [
        "id",
        "special_date",
        "occasion",
        "has_passed",
        "repeats",
        "frequency",
        "foodie",
    ]
    encoders = {"foodie": FoodieEncoder()}


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
        "tagsvo",
        "categoriesvo",
        "eateryimagesvo",
        "allopenhoursvo",
        "reviews",
        "skewered_eateries",
    ]
    encoders = {
        "tagsvo": EateryTagVOEncoder(),
        "categoriesvo": EateryCategoryVOEncoder(),
        "eateryimagesvo": EateryImageVOEncoder(),
        "allopenhoursvo": EateryOpenHoursVOEncoder(),
        "reviews": ReviewEncoder(),
        "skewered_eateries": SkeweredEateryEncoder(),
    }
