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
    ]

    def get_extra_data(self, o):
        eatery_info = {
            "eatery_name": o.eatery_vo.eatery_name,
            "eatery_import_href": o.eatery_vo.import_href,
            "eatery_price": o.eatery_vo.price,
            "eatery_average_rating": o.eatery_vo.average_rating,
            "eatery_location_city": o.eatery_vo.location_city,
            "eatery_location_state": o.eatery_vo.location_state,
            "eatery_latitude": o.eatery_vo.latitude,
            "eatery_longitude": o.eatery_vo.longitude,
        }
        foodie_info = {
            "foodie_username": o.foodie_vo.username,
            "foodie_firstname": o.foodie_vo.first_name,
            "foodie_lastname": o.foodie_vo.last_name,
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


class SpecialDateEncoder(ModelEncoder):
    model = SpecialDate
    properties = [
        "id",
        "special_date",
        "occasion",
        "has_passed",
        "repeats",
        "frequency",
    ]


class FoodieEncoder(ModelEncoder):
    model = FoodieVO
    properties = [
        "username",
        "first_name",
        "email",
        "phone",
        "skewered_eateries",
        "special_dates",
    ]
    encoders = {
        "skewered_eateries": SkeweredEateryEncoder(),
        "special_dates": SpecialDateEncoder(),
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
