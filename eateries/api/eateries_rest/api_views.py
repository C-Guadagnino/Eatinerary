from turtle import title
from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from .models import EateryCategory, EateryLocation, Eatery
from .encoders import EateryEncoder, EateryLocationEncoder, EateryCategoryEncoder
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
        return JsonResponse(
            {"eateries": eateries},
            encoder=EateryEncoder
        )
    #TypeError: Object of type ManyRelatedManager is not JSON serializable
    #Need to fix error when trying to POST with manytomany field relationship
    #Will come back tomorrow and work on this issue
    else:
        # try:
        content = json.loads(request.body)

        print("$$$$$$$$$$$$$$", content)

        categories_list = content["categories"]

        del content["categories"]

        locations_key = content["location"]
        location = EateryLocation.objects.get(id=locations_key)
        content["location"] = location

        eatery = Eatery(**content)
        
        eatery.save()

        category_dict_list = []

        for cat in categories_list:
            cat_title =EateryCategory.objects.get(title=cat)
            eatery.categories.add(cat_title)
            category_dict = json.dumps(cat_title)
            category_dict_list.append(category_dict)
            print("Category Dict LISt", category_dict_list)

        return JsonResponse(
            category_dict_list,
            safe=False,
        ) 
        # return category_dict

        # return JsonResponse(
        #     {"AHHH": "DUMMMMMMY"}
        # )
        # category = EateryCategory.objects.get(id=categories_list)
        # content["categories"] = category

        # print("CATEGORIES:", category)


        # print("Locations:", location)

        # eatery = Eatery.objects.create(**content)

        
        # print("EATERY REQUEST:",eatery)
        # return JsonResponse(
        #     eatery,
        #     encoder=EateryEncoder,
        #     safe=False,
        # )






    # else:
    #     # try:
    #     content = json.loads(request.body)
    #     print("$$$$$$$$$$$$$$", content)
    #     categories_list = content["categories"]
    #     # for ck in categories_list:
    #     #     EateryCategory.objects.get(title=categories_list)
    #     content["categories"] = category
    #     print("CATEGORIES:", category)
    #     locations_key = content["location"]
    #     location = EateryLocation.objects.get(id=locations_key)
    #     content["location"] = location
    #     print("Locations:", location)
    #     eatery = Eatery.objects.create(**content)
    #     if eatery.is_valid():
    #         for category in EateryCategory.objects.all():
    #             category.add(EateryCategory)

        
    #     print("EATERY REQUEST:",eatery)
    #     return JsonResponse(
    #         eatery,
    #         encoder=EateryEncoder,
    #         safe=False,
    #     )
        # except:
        #     response = JsonResponse(
        #         {"message": "Could not create eatery"}
        #     )
        #     response.status_code = 400
        #     return response

@require_http_methods(["GET"])
def api_get_eatery(request, pk):
    if request.method == "GET":
        eatery = Eatery.objects.get(pk=pk)
        print("EATERY IS:", eatery)
        return JsonResponse(
            {"eatery": eatery},
            encoder=EateryEncoder
        )

@require_http_methods(["GET"])
def api_get_location(request, pk):
    if request.method == "GET":
        location = EateryLocation.objects.get(pk=pk)
        print("location IS:", location)
        return JsonResponse(
            {"location": location},
            encoder=EateryLocationEncoder
        )

@require_http_methods(["GET"])
def api_get_category(request, pk):
    if request.method == "GET":
        category = EateryCategory.objects.get(pk=pk)
        print("location IS:", category)
        return JsonResponse(
            {"location": category},
            encoder=EateryCategoryEncoder
        )