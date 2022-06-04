import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from common.json import ModelEncoder
from .models import Foodie
from django.shortcuts import render
from .acls import get_restaurant, get_eatery

class FoodieEncoder(ModelEncoder):
    model = Foodie
    properties = [
        "username",
        "first_name",
        "email",
        "phone",
        "google_calendar",
    ]

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

# @require_http_methods(["GET"])
# def api_get_yelp(request):
#     if request.method == "GET":
#         #If Yelp is running... 
#         try: 
#             restaurant = get_restaurant()
#             #create the yelp search term (normalizing the term, make it lowercase before saving it) .lower()
#             #loop over the list of restaurants
#             # for each restaurant 
#             #create a new YelpSearchResult
#         #If Yelp is down... 
#         except:
#             pass
#             #query the search term 
#             # get the results collection from the search term  
#         return JsonResponse(
#             {"restaurant": restaurant}
#         )


@require_http_methods(["GET"])
def api_get_yelp(request):
    if request.method == "GET":
        restaurant = get_eatery("los angeles", "tacos")
        return JsonResponse(
            {"restaurant": restaurant}
        )


#NEEDS REVIEW
#Get list of all eateries the foodie has skewered
#need a (request,pk) here for the specific foodie?? 
#need to make a SkeweredEateryEncoder! 
# @require_http_methods(["GET"])
# def api_list_skewered_eateries(request):
#     if request.method == "GET":
#         try:
#             skewered_eateries = SkeweredEatery.objects.all()
#             return JsonResponse(
#                 {"skewered_eateries": skewered_eateries},
#                 encoder=SkeweredEateryEncoder,
#                 safe=False
#             )
#         except SkeweredEatery.DoesNotExist:
#             return JsonResponse(
#                 {"message": "Does not exist"},
#                 status=400,
#             )
        

#If we do need the (request,pk)...
#API endpoint update: mySkewered/foodieID? 
# "mySkewered/<int:pk>/", api_list_skewered_eateries, name=""
#<int:pk> would be the foodie id from FK
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


#GET the details for a specific eatery that foodie skewered
#API endpoint: mySkewered/spotID
# api_urls = "mySkewered/eatery/<int:pk>/", api_show_skewered_eatery, name = ""
#NEEDS REVIEW
# @require_http_methods(["GET"])
# def api_show_skewered_eatery(request, pk):
#     if request.method == "GET":
#         try:
#             eatery = SkeweredEatery.objects.filter(eatery=pk)
#             return JsonResponse(
#                 eatery,
#                 encoder=SkeweredEateryEncoder,
#                 safe=False
#             )
#         except SkeweredEatery.DoesNotExist:
#             response = JsonResponse({"message": "Does not exist"})
#             response.status_code = 404
#             return response

