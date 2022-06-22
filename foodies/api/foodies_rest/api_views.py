import djwto.authentication as auth
import json
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# from django.shortcuts import render
from .encoders import (
    FoodieEncoder,
    EateryVOEncoder,
    EateryCategoryVOEncoder,
    EateryTagVOEncoder,
    EateryOpenHoursVOEncoder,
    EateryImageVOEncoder,
    SkeweredEateryEncoder,
    ReviewEncoder,
    ReviewImageEncoder,
    SpecialDateEncoder,
)
from .models import (
    FoodieVO,
    EateryVO,
    EateryCategoryVO,
    EateryTagVO,
    EateryOpenHoursVO,
    EateryImageVO,
    SkeweredEatery,
    Review,
    ReviewImage,
    SpecialDate,
)

# Will only let this view function run if there's a JWT
# in the 'Authorization' header
@auth.jwt_login_required
# @require_http_methods(["GET", "POST"])
def get_foodie_skewers(request):
    return JsonResponse({"received": request.payload})


# List all foodies, create a foodie
@require_http_methods(["GET", "POST"])
def api_foodies(request):
    if request.method == "GET":
        foodie_vo = FoodieVO.objects.all()
        return JsonResponse(
            {"foodies": foodie_vo},
            encoder=FoodieEncoder,
        )
    else:
        content = json.loads(request.body)
        foodie_vo = FoodieVO.objects.create(**content)
        return JsonResponse(
            foodie_vo,
            encoder=FoodieEncoder,
            safe=False,
        )


# List all EateryVOs
@require_http_methods(["GET"])
def api_eateries_vo(request):
    if request.method == "GET":
        try:
            eateries = EateryVO.objects.all()
            return JsonResponse(
                {"eateries": eateries}, encoder=EateryVOEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get details of an EateryVO
@require_http_methods(["GET"])
def api_eatery_vo(request, eatery_entity_id):
    if request.method == "GET":
        try:
            full_import_href = "/api/eateries/" + str(eatery_entity_id) + "/"
            eatery_vo_obj = EateryVO.objects.get(import_href=full_import_href)
            return JsonResponse(eatery_vo_obj, encoder=EateryVOEncoder, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({"message": "Does not exist"}, status=404)


# Get all EateryCategoryVOs
@require_http_methods(["GET"])
def api_categories_vo(request):
    if request.method == "GET":
        try:
            eatery_categories = EateryCategoryVO.objects.all()
            return JsonResponse(
                {"eatery_categories": eatery_categories},
                encoder=EateryCategoryVOEncoder,
                safe=False,
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get a specific details of a EateryCategoryVO
@require_http_methods(["GET"])
def api_category_vo(request, alias):
    if request.method == "GET":
        try:
            category = EateryCategoryVO.objects.get(alias=alias)
            return JsonResponse(category, encoder=EateryCategoryVOEncoder, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get all EateryTagsVO
@require_http_methods(["GET"])
def api_tags_vo(request):
    if request.method == "GET":
        tags = EateryTagVO.objects.all()
        return JsonResponse({"tags": tags}, encoder=EateryTagVOEncoder)


# Get details of an EateryTagVO
@require_http_methods(["GET"])
def api_tag_vo(request, tag_name):
    if request.method == "GET":
        try:
            tag = EateryTagVO.objects.get(tag_name=tag_name)
            return JsonResponse(tag, encoder=EateryTagVOEncoder, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get all OpenHoursVOs
@require_http_methods(["GET"])
def api_eatery_openhours_plural_vo(request):
    if request.method == "GET":
        try:
            eatery_openhours_plural = EateryOpenHoursVO.objects.all()
            return JsonResponse(
                {"eatery_open_hours_all": eatery_openhours_plural},
                encoder=EateryOpenHoursVOEncoder,
                safe=False,
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get specific OpenHoursVO
@require_http_methods(["GET"])
def api_eatery_openhours_singular_vo(request, eatery_openhours_entity_id):
    if request.method == "GET":
        try:
            full_import_href = "/api/openhours/" + str(eatery_openhours_entity_id) + "/"
            eatery_openhours_singular = EateryOpenHoursVO.objects.get(
                import_href=full_import_href
            )
            return JsonResponse(
                eatery_openhours_singular, encoder=EateryOpenHoursVOEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get all EateryImageVOs
@require_http_methods(["GET"])
def api_eatery_images_vo(request):
    if request.method == "GET":
        try:
            eatery_images = EateryImageVO.objects.all()
            return JsonResponse(
                {"eatery_images": eatery_images},
                encoder=EateryImageVOEncoder,
                safe=False,
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# Get specific EateryImageVO
@require_http_methods(["GET"])
def api_eatery_image_vo(request, eatery_image_entity_id):
    if request.method == "GET":
        try:
            full_import_href = "/api/eateryimages/" + str(eatery_image_entity_id) + "/"
            eatery_image = EateryImageVO.objects.get(import_href=full_import_href)
            return JsonResponse(eatery_image, encoder=EateryImageVOEncoder, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )


# List skewered eateries & Add eatery to skewered list
@require_http_methods(["GET", "POST"])
def api_skewered_eateries(request):
    if request.method == "GET":
        try:
            skewered_eateries = SkeweredEatery.objects.all()
            return JsonResponse(
                {"skewered_eateries": skewered_eateries},
                encoder=SkeweredEateryEncoder,
                safe=False,
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )
    else:
        try:
            content = json.loads(request.body)

            eateryvo_import_href = content["eateryvo_import_href"]
            eateryvo_obj = EateryVO.objects.get(import_href=eateryvo_import_href)
            content["eatery_vo"] = eateryvo_obj
            del content["eateryvo_import_href"]

            foodie_username = content["foodie_vo"]
            foodie_obj = FoodieVO.objects.get(username=foodie_username)
            content["foodie_vo"] = foodie_obj

            content["is_active"] = True
            content["has_visited"] = False

            skewered_eatery = SkeweredEatery.objects.create(**content)

            return JsonResponse(
                skewered_eatery, encoder=SkeweredEateryEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Could not create the skewered eatery"},
                status=400,
            )


# Get details of a skewered eatery
@require_http_methods(["GET", "DELETE", "PUT"])
def api_skewered_eatery(request, pk):
    if request.method == "GET":
        try:
            skewered_eatery = SkeweredEatery.objects.get(id=pk)
            return JsonResponse(
                {"skewered_eatery": skewered_eatery},
                encoder=SkeweredEateryEncoder,
                safe=False,
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )
    elif request.method == "DELETE":
        skewered_eatery = SkeweredEatery.objects.filter(id=pk).update(is_active=False)
        return JsonResponse(
            skewered_eatery,
            encoder=SkeweredEateryEncoder,
            safe=False,
        )
    else:
        try:
            content = json.loads(request.body)
            SkeweredEatery.objects.filter(id=pk).update(**content)
            skewered_eatery = SkeweredEatery.objects.get(id=pk)
            return JsonResponse(
                skewered_eatery, encoder=SkeweredEateryEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse({"message": "Does not exist"}, status=404)
#======================================

@require_http_methods(["GET"])
def api_show_skeweredeateries_for_specific_foodie(request, username):
    if request.method == "GET":
        try:
            foodie = SkeweredEatery.objects.filter(foodie_vo=username)
            return JsonResponse(
                {"skewered_eateries":foodie},
                encoder=SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response

#======================================

# List all foodie reviews, create review
@require_http_methods(["GET", "POST"])
def api_reviews(request):
    if request.method == "GET":
        reviews = Review.objects.all()
        return JsonResponse({"reviews": reviews}, encoder=ReviewEncoder, safe=False)

    else:
        try:
            content = json.loads(request.body)

            skewered_eatery_id = content["skewered_eatery"]
            skewered_eatery_obj = SkeweredEatery.objects.get(id=skewered_eatery_id)
            content["skewered_eatery"] = skewered_eatery_obj

            eatery_vo_obj = EateryVO.objects.get(
                import_href=skewered_eatery_obj.eatery_vo.import_href
            )
            content["eatery_vo"] = eatery_vo_obj

            review = Review.objects.create(**content)

            return JsonResponse(review, encoder=ReviewEncoder, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Could not create the skewered eatery"},
                status=400,
            )


# Get details of a specific review
@require_http_methods(["GET", "DELETE", "PUT"])
def api_review(request, pk):
    if request.method == "GET":
        try:
            foodie_review = Review.objects.get(id=pk)
            return JsonResponse(
                {"foodie_review": foodie_review}, encoder=ReviewEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )
    elif request.method == "DELETE":
        count, _ = Review.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        try:
            content = json.loads(request.body)

            Review.objects.filter(id=pk).update(**content)
            foodie_review = Review.objects.get(id=pk)
            return JsonResponse(foodie_review, encoder=ReviewEncoder, safe=False)
        # TO-DO: Figure out what kind of error this throws
        except:
            return JsonResponse(
                {"message": "Cannot update skewered eatery"}, status=400
            )


# List all review images, create a review image
@require_http_methods(["GET", "POST"])
def api_review_images(request):
    if request.method == "GET":
        review_images = ReviewImage.objects.all()
        return JsonResponse(
            {"review_images": review_images}, encoder=ReviewImageEncoder, safe=False
        )
    else:
        try:
            content = json.loads(request.body)

            review_id = content["review"]
            review = Review.objects.get(id=review_id)
            content["review"] = review
            review_image = ReviewImage.objects.create(**content)

            return JsonResponse(review_image, encoder=ReviewImageEncoder, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Cannot create review image before creating review"},
                status=400,
            )


# Get a specific review image
@require_http_methods(["GET", "DELETE"])
def api_review_image(request, pk):
    if request.method == "GET":
        try:
            review_image = ReviewImage.objects.get(id=pk)
            return JsonResponse(
                {"review_image": review_image}, encoder=ReviewImageEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Review image does not exist"},
                status=404,
            )
    else:
        count, _ = ReviewImage.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})


# List all foodie reviews, create review
@require_http_methods(["GET", "POST"])
def api_special_dates(request, foodie_id=None):
    if request.method == "GET":
        if foodie_id == None:
            special_dates = SpecialDate.objects.all()
        else:
            foodie_obj = FoodieVO.objects.get(id=foodie_id)
            special_dates = SpecialDate.objects.filter(foodie=foodie_obj)
        return JsonResponse(
            {"special_dates": special_dates}, encoder=SpecialDateEncoder, safe=False
        )

    else:
        try:
            content = json.loads(request.body)

            foodie_id = content["foodie_vo"]
            foodie_obj = FoodieVO.objects.get(id=foodie_id)
            content["foodie_vo"] = foodie_obj

            special_date_obj = SpecialDate.objects.create(**content)

            return JsonResponse(
                special_date_obj, encoder=SpecialDateEncoder, safe=False
            )
        except:
            return JsonResponse(
                {"message": "Could not create the Special Date"},
                status=400,
            )


# Get details of a specific review
@require_http_methods(["GET", "DELETE", "PUT"])
def api_special_date(request, pk):
    if request.method == "GET":
        try:
            special_date = SpecialDate.objects.get(id=pk)
            return JsonResponse(
                {"special_date": special_date}, encoder=SpecialDateEncoder, safe=False
            )
        except ObjectDoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=404,
            )
    elif request.method == "DELETE":
        count, _ = SpecialDate.objects.filter(id=pk).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        try:
            content = json.loads(request.body)

            SpecialDate.objects.filter(id=pk).update(**content)
            special_date = SpecialDate.objects.get(id=pk)
            return JsonResponse(special_date, encoder=SpecialDateEncoder, safe=False)
        # TO-DO: Figure out what kind of error this throws
        except:
            return JsonResponse({"message": "Cannot update special date"}, status=400)
