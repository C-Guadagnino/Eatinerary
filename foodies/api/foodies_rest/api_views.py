import djwto.authentication as auth
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .encoders import (
    EateryTagVOEncoder,
    EateryCategoryVOEncoder,
    EateryImageVOEncoder,
    FoodieEncoder,
    EateryVOEncoder,
    SkeweredEateryEncoder,
    ReviewEncoder,
    ReviewImageEncoder,
)
from .models import (
    EateryTagVO,
    EateryCategoryVO,
    EateryImageVO,
    Foodie,
    EateryVO,
    SkeweredEatery,
    Review,
    ReviewImage,
)
from django.shortcuts import render


@require_http_methods(["GET", "POST"])
def api_list_foodies(request):
    if request.method == "GET":
        foodie = Foodie.objects.all()
        return JsonResponse(
            {"foodies": foodie},
            encoder=FoodieEncoder,
        )
    else:
        content = json.loads(request.body)
        foodie = Foodie.objects.create(**content)
        return JsonResponse(
            foodie,
            encoder=FoodieEncoder,
            safe=False,
        )


# Will only let this view function run if there's a JWT
# in the 'Authorization' header
@auth.jwt_login_required
# @require_http_methods(["GET", "POST"])
def get_foodie_skewers(request):
    return JsonResponse({"received": request.payload})


# For EateryVO
@require_http_methods(["GET"])
def api_list_eateries_vo(request):
    if request.method == "GET":
        try:
            eateries = EateryVO.objects.all()
            return JsonResponse(
                {"eateries": eateries}, 
                encoder=EateryVOEncoder, 
                safe=False
            )
        except EateryVO.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400,
            )


# For EateryTagsVO
@require_http_methods(["GET"])
def api_list_tags_vo(request):
    if request.method == "GET":
        try:
            tags = EateryTagVO.objects.all()
            return JsonResponse(
                {"tags": tags}, 
                encoder=EateryTagVOEncoder, 
                safe=False
            )
        except EateryTagVO.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400,
            )

#List skewered eateries & Add eatery to skewered list
@require_http_methods(["GET", "POST"])
def api_list_create_skewered_eatery(request):
    if request.method == "GET":
        try:
            skewered_eatery = SkeweredEatery.objects.all()
            return JsonResponse(
                {"skewered_eatery": skewered_eatery},
                encoder = SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400,
            )
    else: 
        try:
            content = json.loads(request.body)

            eatery_href = content["eatery"]
            eateryvo_obj = EateryVO.objects.get(import_href=eatery_href)
            content["eatery"] = eateryvo_obj

            foodie_username = content["foodie"]
            foodie_obj = Foodie.objects.get(username= foodie_username)
            content["foodie"] = foodie_obj
            skewered_eatery = SkeweredEatery.objects.create(**content)

            return JsonResponse(
                skewered_eatery,
                encoder=SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            return JsonResponse(
                {"message": "Could not create the skewered eatery"},
                status = 400,
            )

#Get details of a skewered eatery
@require_http_methods(["GET"])
def api_get_details_of_skewered_eatery(request,pk):
    if request.method == "GET":
        try:
            skewered_eatery = SkeweredEatery.objects.get(id=pk)
            return JsonResponse(
                {"skewered_eatery": skewered_eatery},
                encoder = SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400,
            )

#Delete or update a skewered eatery
@require_http_methods(["DELETE", "PUT"])
def api_delete_update_skewered_eatery(request,pk):
    if request.method == "DELETE":
        try:
            skewered_eatery = SkeweredEatery.objects.filter(id=pk).update(is_active=False)
            return JsonResponse(
                skewered_eatery,
                encoder=SkeweredEateryEncoder,
                safe=False,
            )
        except SkeweredEatery.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
            )
    else:
        try:
            content = json.loads(request.body)
            print("CONTENT IS!!!!:", content)
            SkeweredEatery.objects.filter(id=pk).update(**content)
            skewered_eatery = SkeweredEatery.objects.get(id=pk)
            return JsonResponse(
                skewered_eatery,
                encoder=SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            return JsonResponse(
                {"message": "Cannot update skewered eatery"},
                status=404
            )


#List all foodie reviews, create review
@require_http_methods(["GET", "POST"])
def api_list_create_review(request):
    if request.method == "GET":
        try:
            reviews = Review.objects.all()
            return JsonResponse(
                {"reviews": reviews},
                encoder=ReviewEncoder,
                safe=False
            )
        except Review.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400
            )
    else:
        try:
            content = json.loads(request.body)
            skewered_restaurant_id = content["skewered_restaurant"]
            skewered_restaurant = SkeweredEatery.objects.get(id=skewered_restaurant_id)
            content["skewered_restaurant"] = skewered_restaurant
            review = Review.objects.create(**content)

            return JsonResponse(
                review,
                encoder=ReviewEncoder,
                safe=False
            )
        except Review.DoesNotExist:
            return JsonResponse(
                {"message": "Could not create the skewered eatery"},
                status = 400,
            )


#Review Image
@require_http_methods(["GET"])
def api_list_all_review_images(request):
    if request.method == "GET":
        #try:
        reviews = ReviewImage.objects.all()
        return JsonResponse(
            {"reviews": reviews},
            encoder=ReviewImageEncoder,
            safe=False
        )


# #Get details of a specific review 
# @require_http_methods(["GET"])
# def api_get_details_of_review(request,pk):
#     if request.method == "GET":
#         try:
#             foodie_review = Review.objects.get(id=pk)
#             return JsonResponse(
#                 {"foodie_review": foodie_review},
#                 encoder=ReviewEncoder,
#                 safe=False
#             )
#         except Review.DoesNotExist:
#             return JsonResponse(
#                 {"message": "Does not exist"},
#                 status=400,
#             )


# #Delete or Update a Review
# @require_http_methods(["DELETE", "PUT"])
# def api_delete_update_review(request,pk):
#     if request.method == "DELETE":
#         try:
#             foodie_review = Review.objects.get(id=pk)
#             foodie_review.delete()
#             return JsonResponse(
#                 foodie_review,
#                 encoder=ReviewEncoder,
#                 safe=False,
#             )
#         except Review.DoesNotExist:
#             return JsonResponse(
#                 {"message": "Does not exist"},
#             )
#     else:
#         try:
#             content = json.loads(request.body)
            
#             Review.objects.filter(id=pk).update(**content)
#             foodie_review = Review.objects.get(id=pk)
#             return JsonResponse(
#                 foodie_review,
#                 encoder=ReviewEncoder,
#                 safe=False
#             )
#         except Review.DoesNotExist:
#             return JsonResponse(
#                 {"message": "Cannot update skewered eatery"},
#                 status=404
#             )

            


