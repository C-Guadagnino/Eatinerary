from turtle import title
from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from .models import EateryCategory, EateryLocation, Eatery
from .encoders import EateryEncoder, EateryLocationEncoder, EateryCategoryEncoder
from .acls import get_eateries_from_yelp

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
        restaurants = get_eateries_from_yelp("los angeles", "tacos")
        return JsonResponse({"restaurants": restaurants})


@require_http_methods(["GET", "POST"])
def api_eateries(request):
    if request.method == "GET":
        eateries = Eatery.objects.all()
        return JsonResponse({"eateries": eateries}, encoder=EateryEncoder)

    else:
        try:
            content = json.loads(request.body)
            categories_list = content["categories"]
            del content["categories"]

            location_id = content["location"]
            location = EateryLocation.objects.get(id=location_id)
            content["location"] = location
            # eatery = Eatery(**content)
            # eatery.save()

            eatery = Eatery.objects.create(**content)

            for cat_title in categories_list:
                cat_obj = EateryCategory.objects.get(title=cat_title)
                eatery.categories.add(cat_obj)

            return JsonResponse(
                eatery,
                encoder=EateryEncoder,
                safe=False,
            )
        except:
            response = JsonResponse({"message": "Could not create eatery"})
            response.status_code = 400
            return response


@require_http_methods(["GET"])
def api_eatery(request, pk):
    if request.method == "GET":
        eatery = Eatery.objects.get(pk=pk)
        print("EATERY IS:", eatery)
        return JsonResponse(eatery, encoder=EateryEncoder, safe=False)


@require_http_methods(["GET", "POST"])
def api_locations(request):
    if request.method == "GET":
        locations = EateryLocation.objects.all()
        return JsonResponse({"locations": locations}, encoder=EateryLocationEncoder)

    else:
        try:
            content = json.loads(request.body)
            location = EateryLocation.objects.create(**content)
            return JsonResponse(location, encoder=EateryLocationEncoder, safe=False)
        except IntegrityError:
            response = JsonResponse(
                {"message": "Could not create location; this location already exists."}
            )
            response.status_code = 400
            return response


@require_http_methods(["GET"])
def api_location(request, pk):
    if request.method == "GET":
        location = EateryLocation.objects.get(pk=pk)
        print("location IS:", location)
        return JsonResponse(location, encoder=EateryLocationEncoder, safe=False)


@require_http_methods(["GET"])
def api_category(request, pk):
    if request.method == "GET":
        category = EateryCategory.objects.get(pk=pk)
        print("location IS:", category)
        return JsonResponse(category, encoder=EateryCategoryEncoder, safe=False)
