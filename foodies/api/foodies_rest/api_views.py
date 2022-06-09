import djwto.authentication as auth
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .encoders import (
    EateryTagVOEncoder, 
    EateryCategoriesVOEncoder,  
    ImageVOEncoder, 
    FoodieEncoder, 
    EateryVOEncoder, 
    SkeweredEateryEncoder, 
    ReviewEncoder)
from .models import (
    EateryTagVO, 
    EateryCategoriesVO, 
    ImageVO, 
    Foodie, 
    EateryVO, 
    SkeweredEatery, 
    Review)
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
#@require_http_methods(["GET", "POST"])
def get_foodie_skewers(request):
    return JsonResponse({"received": request.payload})


# NEEDS REVIEW

#api_show_eateries

#api_add/create_skewered_eateries 
#api_list_skewered_eateries (all instances of eateries)
#api_show_skewered_eatery (detailed instance of 1 eatery)
#api_delete_skewered_eatery
#api_update_skewered_eatery (??)

#api_show_skewered_history

#api_foodie_create_review
#api_foodie_list_reviews
#api_foodie_show_review 


#Get list of all eateries the foodie has skewered
#need a (request,pk) here for the specific foodie??
@require_http_methods(["GET"])
def api_list_skewered_eateries(request):
    if request.method == "GET":
        try:
            skewered_eateries = SkeweredEatery.objects.all()
            return JsonResponse(
                {"skewered_eateries": skewered_eateries},
                encoder=SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            return JsonResponse(
                {"message": "Does not exist"},
                status=400,
            )

#For EateryVO
@require_http_methods(["GET"])
def api_list_eateries(request):
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



# If we do need the (request,pk)...
# API endpoint update: mySkewered/foodieID?
# "mySkewered/<int:pk>/", api_list_skewered_eateries, name=""
# <int:pk> would be the foodie id from FK
# @require_http_methods(["GET"])
# def api_list_skewered_eateries(request, pk):
#     if request.method == "GET":
#         try:
#             foodie = SkeweredEatery.objects.filter(foodie=pk)
#             return JsonResponse(
#                 foodie,
#                 encoder=SkeweredEateryEncoder,
#                 safe=False
#             )
#         except SkeweredEatery.DoesNotExist:
#             response = JsonResponse({"message": "Does not exist"})
#             response.status_code = 404
#             return response


# GET the details for a specific eatery that foodie skewered
# API endpoint: mySkewered/spotID
# api_urls = "mySkewered/eatery/<int:pk>/", api_show_skewered_eatery, name = ""
# NEEDS REVIEW
@require_http_methods(["GET"])
def api_show_skewered_eatery(request, pk):
    if request.method == "GET":
        try:
            eatery = SkeweredEatery.objects.filter(eatery=pk)
            return JsonResponse(
                eatery,
                encoder=SkeweredEateryEncoder,
                safe=False
            )
        except SkeweredEatery.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
