from common.json import ModelEncoder
from .models import (
    EateryTagVO,
    EateryCategoryVO,
    EateryImageVO,
    Foodie,
    EateryVO,
    ReviewImage,
    SkeweredEatery,
    Review,
)


class EateryCategoryVOEncoder(ModelEncoder):
    model = EateryCategoryVO
    properties = ["import_href", "alias", "title"]

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery_vo.eatery_name,
                "eatery_import_href": o.eatery_vo.import_href,
            }
        }


class EateryImageVOEncoder(ModelEncoder):
    model = EateryImageVO
    properties = ["import_href", "image_url"]

    def get_extra_data(self, o):
        return {
            "eatery": {
                "eatery_name": o.eatery_vo.eatery_name,
                "eatery_import_href": o.eatery_vo.import_href,
            }
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


# class EateryTagVOEncoder(ModelEncoder):
#     model = EateryTagVO
#     properties = ["import_href", "tag_name", "eatery_vo"]
#     encoders = {
#         "eatery_vo": EateryVOEncoder(),
#     }

#     # def get_extra_data(self, o):
#     #     return {
#     #         "eatery": {
#     #             "eatery_name": o.eatery_vo,
#     #             "eatery_import_href": o.eatery_vo,
#     #         }
#     #     }


class EateryTagVOEncoder(ModelEncoder):
    model = EateryTagVO
    properties = ["import_href", "tag_name"]

    def get_extra_data(self, o):
        eateries = []
        for eatery in o.eatery_vo.all():
            eatery_dict = {}
            eatery_dict["eatery_name"] = eatery.eatery_name
            eatery_dict["eatery_import_href"] = eatery.import_href
            eateries.append(eatery_dict)

        return {"eateries": eateries}


# class EateryTagVOEncoder(ModelEncoder):
#     model = EateryTagVO
#     properties = ["import_href", "tag_name", "eatery_vo"]
#     encoders = {
#         "eatery_vo": EateryVOEncoder(),
#     }


#     # def get_extra_data(self, o):
#     #     return {
#     #         "eatery": {
#     #             "eatery_name": o.eatery_vo,
#     #             "eatery_import_href": o.eatery_vo,
#     #         }
#     #     }


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
    ]
    encoders = {
        "tagsvo": EateryTagVOEncoder(),
        "categoriesvo": EateryCategoryVOEncoder(),
    }


class SkeweredEateryEncoder(ModelEncoder):
    model = SkeweredEatery
    properties = [
        "id",
        "eatery_vo",
        "foodie",
        "created_DateTime",
        "updated_DateTime",
        "has_visited",
        "is_active",
        "notes",
    ]
    encoders = {
        "eatery_vo": EateryVOEncoder(),
        "foodie": FoodieEncoder(),
    }


class ReviewImageEncoder(ModelEncoder):
    model = ReviewImage
    properties = ["id", "image_url"]

    def get_extra_data(self, o):
        return {"review": {"title": o.review.title, "review_id": o.review.id}}


class ReviewEncoder(ModelEncoder):
    model = Review
    properties = [
        "id",
        "title",
        "rating",
        "created_DateTime",
        "description",
        "eatery_vo",
        "skewered_eatery",
        # "review_images"
    ]
    encoders = {
        "eatery_vo": EateryVOEncoder(),
        "skewered_eatery": SkeweredEateryEncoder(),
        # "review_images": ReviewImageEncoder()
    }
