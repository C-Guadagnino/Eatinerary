from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from common.json import ModelEncoder
from django.shortcuts import render
from .acls import get_restaurants, get_eateries


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
