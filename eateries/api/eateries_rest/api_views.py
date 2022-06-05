from turtle import title
from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from .models import EateryCategory, EateryLocation, Eatery
from .encoders import EateryEncoder
from .acls import get_eateries

# @require_http_methods(["GET"])
# def api_get_yelp(request):
#     if request.method == "GET":
#         #If Yelp is running...
#         try:
#             restaurant = get_restaurants()
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
        restaurant = get_eateries("los angeles", "tacos")
        return JsonResponse({"restaurant": restaurant})

@require_http_methods(["GET", "POST"])
def api_get_eatery_data(request):
    if request.method == "GET":
        eateries = Eatery.objects.all()
        print(eateries)
        return JsonResponse(
            {"eateries": eateries},
            encoder=EateryEncoder
        )
    # else:
    #     try:
    #         content = json.loads(request.body)
    #         print("$$$$$$$$$$$$$$", content)
    #         title = content["title"]
    #         category = EateryCategory.objects.get(pk=title)
    #         content["model"] = category
    #         zip = content["zip"]
    #         location = EateryLocation.objects.get(pk=zip)
    #         content["model"] = location
    #         eatery = Eatery.objects.create(**content)
    #         return JsonResponse(
    #             eatery,
    #             encoder=EateryEncoder,
    #             safe=False,
    #         )
    #     except:
    #         response = JsonResponse(
    #             {"message": "Could not create eatery"}
    #         )
    #         response.status_code = 400
    #         return response
