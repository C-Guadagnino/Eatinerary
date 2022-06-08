from turtle import title
from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from .models import EateryCategory, EateryImage, EateryLocation, Eatery, Tag, EateryOpenHours, EateryImage, WEEKDAYS
from .encoders import EateryEncoder, EateryLocationEncoder, EateryCategoryEncoder, TagEncoder, OpenHoursEncoder, EateryImageEncoder
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


#For some reason the POST method creates an instance of Eatery even though the request returns a 400 error.
@require_http_methods(["GET", "POST"])
def api_eateries(request):
    if request.method == "GET":
        eateries = Eatery.objects.all()
        return JsonResponse({"eateries": eateries}, encoder=EateryEncoder)

    else:
        # try:
        content = json.loads(request.body)
        categories_list = content["categories"]
        tags_list = content["tags"]

        del content["categories"]
        del content["tags"]

        location_id = content["location"]
        location = EateryLocation.objects.get(id=location_id)
        content["location"] = location

        # eatery = Eatery(**content)
        # eatery.save()

        eatery = Eatery.objects.create(**content)

        for cat_title in categories_list:
            cat_obj = EateryCategory.objects.get(title=cat_title)
            eatery.categories.add(cat_obj)
        
        for tag_name in tags_list:
            tag_obj = Tag.objects.get(tag_name=tag_name)
            eatery.tags.add(tag_obj)

        return JsonResponse(
            eatery,
            encoder=EateryEncoder,
            safe=False,
        )
        # except:
        #     response = JsonResponse({"message": "Could not create eatery"})
        #     response.status_code = 400
        #     return response



@require_http_methods(["GET", "PUT"])
def api_eatery(request, pk):
    if request.method == "GET":
        eatery = Eatery.objects.get(pk=pk)
        print("EATERY IS:", eatery)
        return JsonResponse(eatery, encoder=EateryEncoder, safe=False)
    else:
        content = json.loads(request.body)
        tags_list_single_item = content["tags"]
        eatery = Eatery.objects.get(pk=pk)
        for tag_name in tags_list_single_item:
            tag_obj = Tag.objects.get(tag_name=tag_name)
            eatery.tags.add(tag_obj)
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
        return JsonResponse(category, encoder=EateryCategoryEncoder, safe=False)





@require_http_methods(["GET", "POST"])
def api_categories(request):
    if request.method == "GET":
        categories = EateryCategory.objects.all()
        return JsonResponse({"categories": categories}, encoder=EateryCategoryEncoder)
    else:
        try:
            content = json.loads(request.body)
            category = EateryCategory.objects.create(**content)
            return JsonResponse(category, encoder=EateryCategoryEncoder, safe=False)
        except IntegrityError:
            response = JsonResponse(
                {"message": "Could not create category; this category already exists."}
            )
            response.status_code = 400
            return response



@require_http_methods(["GET", "POST"])
def api_tags(request):
    if request.method == "GET":
        tags = Tag.objects.all()
        return JsonResponse({"tags": tags}, encoder=TagEncoder)
    else:
        try:
            content = json.loads(request.body)
            tag = Tag.objects.create(**content)
            return JsonResponse(tag, encoder=TagEncoder, safe=False)
        except IntegrityError:
            response = JsonResponse(
                {"message": "Could not create tag; this tag already exists."}
            )
            response.status_code = 400
            return response






@require_http_methods(["GET", "POST"])
def api_open_hours_plural(request):
    if request.method == "GET":
        open_hours_all = EateryOpenHours.objects.all()
        return JsonResponse({"open_hours": open_hours_all}, encoder=OpenHoursEncoder)
    else:
        try:
            content = json.loads(request.body)
            eatery_id = content["eatery"]
            eatery = Eatery.objects.get(pk=eatery_id)
            content["eatery"] = eatery
            open_hours_one = EateryOpenHours.objects.create(**content)
            
            return JsonResponse(open_hours_one, encoder=OpenHoursEncoder, safe=False)
        except IntegrityError:
            response = JsonResponse(
                {"message": "Could not create open hours"}
            )
            response.status_code = 400
            return response

@require_http_methods(["GET"])
def api_open_hours_singular(request, pk):
    if request.method == "GET":
        open_hours_singular = EateryOpenHours.objects.get(pk=pk)
        return JsonResponse(open_hours_singular, encoder=OpenHoursEncoder, safe=False)


@require_http_methods(["GET", "POST"])
def api_eatery_images(request):
    if request.method == "GET":
        eatery_images = EateryImage.objects.all()
        return JsonResponse({"eatery_images": eatery_images}, encoder=EateryImageEncoder)
    else:
        try:
            content = json.loads(request.body)
            eatery_id = content["eatery"]
            eatery = Eatery.objects.get(pk=eatery_id)
            content["eatery"] = eatery
            print("THIS IS EATERY!!!", eatery)
            eatery_image = EateryImage.objects.create(**content)
            return JsonResponse(eatery_image, encoder=EateryImageEncoder, safe=False)
        except IntegrityError:
            response = JsonResponse(
                {"message": "Could not create eatery image"}
            )
            response.status_code = 400
            return response

@require_http_methods(["GET"])
def api_eatery_image(request, pk):
    if request.method == "GET":
        eatery_image = EateryImage.objects.get(pk=pk)
        return JsonResponse(eatery_image, encoder=EateryImageEncoder, safe=False)