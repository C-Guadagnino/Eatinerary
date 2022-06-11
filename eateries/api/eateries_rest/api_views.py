from turtle import title
from django.shortcuts import render
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from .models import (
    EateryCategory,
    EateryImage,
    EateryLocation,
    Eatery,
    Tag,
    EateryOpenHours,
    EateryImage,
    WEEKDAYS,
    YelpLocationSearchTerm,
    YelpCategorySearchTerm,
    YelpResult,
)
from .encoders import (
    EateryEncoder,
    EateryLocationEncoder,
    EateryCategoryEncoder,
    TagEncoder,
    OpenHoursEncoder,
    EateryImageEncoder,
    YelpLocationSearchTermEncoder,
    YelpCategorySearchTermEncoder,
    YelpResultEncoder
)
from .acls import get_eateries_from_yelp, get_restaurants, get_details_of_one_eatery

# distinct? database thing?
@require_http_methods(["GET"])
def api_return_list_of_restaurants_given_category_and_location(
    request, location, category
):
    if request.method == "GET":
        #Send request to Yelp API to get a list of eateries given category and location
        eateries_dictionary = get_eateries_from_yelp(location, category)
        # Create location search term object if it doesn't already exist
        try:
            location_searchterm_obj = YelpLocationSearchTerm.objects.create(
                location_term=location
            )
        except IntegrityError:
            pass
        # Create category search term object if it doesn't already exist
        try:
            category_searchterm_obj = YelpCategorySearchTerm.objects.create(
                category_term=category
            )
        except IntegrityError:
            pass 

        eateries_list = eateries_dictionary["businesses"]
        for eatery in eateries_list:

            if eatery["location"]["display_address"]:
                del eatery["location"]["display_address"]

            location_dict = eatery["location"]
            location_obj = EateryLocation.objects.create(**location_dict)

            categories_list = eatery["categories"]

            for category_dict in categories_list:
                category_obj = EateryCategory.objects.update_or_create(
                    alias=category_dict["alias"],
                    defaults={
                        "title": category_dict["title"]
                    }
                )
            #check if the current eatery already exists in our database
            try:
                Eatery.objects.get(yelp_id=eatery["id"])
            #if it doesn't exist lets create it
            except ObjectDoesNotExist:
                eatery_name = eatery["name"]
                phone = eatery["display_phone"]
                latitude = eatery["coordinates"]["latitude"]
                longitude = eatery["coordinates"]["longitude"]
                website = eatery["url"]
                yelp_id = eatery["id"]
                review_count = eatery["review_count"]
                average_rating = eatery["rating"]
                from_yelp = "True"
                if "price" in eatery:
                    price = eatery["price"]
                    eatery_dict = {
                        "eatery_name": eatery_name,
                        "website": website,
                        "latitude": latitude,
                        "longitude": longitude,
                        "phone": phone,
                        "yelp_id": yelp_id,
                        "review_count": review_count,
                        "average_rating": average_rating,
                        "location": location_obj,
                        "from_yelp": from_yelp,
                        "price": price,
                    }
                else:
                    eatery_dict = {
                        "eatery_name": eatery_name,
                        "website": website,
                        "latitude": latitude,
                        "longitude": longitude,
                        "phone": phone,
                        "yelp_id": yelp_id,
                        "review_count": review_count,
                        "average_rating": average_rating,
                        "location": location_obj,
                        "from_yelp": from_yelp,
                    }
                eatery_obj = Eatery.objects.create(**eatery_dict)

                # Loop through list of categories to create a relationship to the current eatery
                for category_dict in categories_list:
                    category_obj = EateryCategory.objects.get(alias=category_dict["alias"])
                    eatery_obj.categories.add(category_obj)

                # Create relationship between the image url and the current eatery
                image_url = eatery["image_url"]
                EateryImage.objects.create(image_url=image_url, eatery=eatery_obj)
                image_obj = EateryImage.objects.get(image_url=image_url)

                # Send request to yelp api with function call to get the details of the current eatery
                # to specifically access the open hours
                current_eatery_yelp_id = eatery_obj.yelp_id
                eatery_details_dict = get_details_of_one_eatery(current_eatery_yelp_id)

                # if an eatery has hours then create EateryOpenHours objects and create a relationship
                # to the current eatery.
                try:
                    open_hours_list = eatery_details_dict["hours"][0]["open"]
                    for open_hours_singular in open_hours_list:
                        initial_start_time = open_hours_singular["start"]
                        # "1130"
                        start_time = initial_start_time[:2:] + ":" + initial_start_time[2::]
                        initial_end_time = open_hours_singular["end"]
                        # "1130"
                        end_time = initial_end_time[:2:] + ":" + initial_end_time[2::]
                        initial_day = open_hours_singular["day"]
                        # "1130"
                        weekday = initial_day + 1

                        open_hours_dict= {
                            "eatery": eatery_obj,
                            "weekday": weekday,
                            "start_time": start_time,
                            "end_time": end_time,
                        }

                        open_hours_singular_obj = EateryOpenHours.objects.create(**open_hours_dict)
                except KeyError:
                    pass
            
            # If YelpResult object with the location category and eatery doesn't already exist then create it
            try:
                yelp_result_dict = {
                    "location_term": YelpLocationSearchTerm.objects.get(location_term=location),
                    "category_term": YelpCategorySearchTerm.objects.get(category_term=category),
                    "eatery": Eatery.objects.get(yelp_id=eatery["id"])
                }
                yelp_result_obj = YelpResult.objects.create(**yelp_result_dict)
            except IntegrityError:
                pass
        return JsonResponse({"eateries": eateries_dictionary})

@require_http_methods(["GET"])
def api_yelp_result(request):
    if request.method == "GET":
        yelp_results = YelpResult.objects.all()
        return JsonResponse({"yelp_results": yelp_results},
        encoder=YelpResultEncoder)

@require_http_methods(["GET"])
def api_yelp_location_search_terms(request):
    if request.method == "GET":
        location_search_terms = YelpLocationSearchTerm.objects.all()
        return JsonResponse({"location_search_terms": location_search_terms},
        encoder=YelpLocationSearchTermEncoder)

@require_http_methods(["GET"])
def api_yelp_category_search_terms(request):
    if request.method == "GET":
        category_search_terms = YelpCategorySearchTerm.objects.all()
        return JsonResponse({"category_search_terms": category_search_terms},
        encoder=YelpCategorySearchTermEncoder)

@require_http_methods(["GET"])
def api_get_yelp_with_category_and_location(request, location, category):
    if request.method == "GET":
        restaurants = get_eateries_from_yelp(location, category)
        return JsonResponse({"restaurants": restaurants})


@require_http_methods(["GET"])
def api_get_yelp_with_location(request, location):
    if request.method == "GET":
        restaurants = get_restaurants(location)
        return JsonResponse({"restaurants": restaurants})

@require_http_methods(["GET"])
def api_get_yelp_one_eatery(request, yelp_id):
    if request.method == "GET":
        eatery_details_dict = get_details_of_one_eatery(yelp_id)
        print("Eatery Dictionary", eatery_details_dict)
        open_hours_list = eatery_details_dict["hours"][0]["open"]
        for open_hours_singular in open_hours_list:
            initial_start_time = open_hours_singular["start"]
            # "1130"
            start_time = initial_start_time[:2:] + ":" + initial_start_time[2::]
            initial_end_time = open_hours_singular["end"]
            # "1130"
            end_time = initial_end_time[:2:] + ":" + initial_end_time[2::]
            initial_day = open_hours_singular["day"]
            # "1130"
            weekday = initial_day + 1
            print("Week Day Index", weekday)
        return JsonResponse({"eatery_details_dic": eatery_details_dict})


# For some reason the POST method creates an instance of Eatery even though the request returns a 400 error.
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

        for cat_alias in categories_list:
            cat_obj = EateryCategory.objects.get(alias=cat_alias)
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


@require_http_methods(["GET"])
def api_tag(request, pk):
    if request.method == "GET":
        tag = Tag.objects.get(pk=pk)
        return JsonResponse(tag, encoder=TagEncoder, safe=False)


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
            response = JsonResponse({"message": "Could not create open hours"})
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
        return JsonResponse(
            {"eatery_images": eatery_images}, encoder=EateryImageEncoder
        )
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
            response = JsonResponse({"message": "Could not create eatery image"})
            response.status_code = 400
            return response


@require_http_methods(["GET"])
def api_eatery_image(request, pk):
    if request.method == "GET":
        eatery_image = EateryImage.objects.get(pk=pk)
        return JsonResponse(eatery_image, encoder=EateryImageEncoder, safe=False)
