import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owners_project.settings")
django.setup()

from owners_rest.models import (
    EateryVO,
    EateryTagVO,
    EateryCategoryVO,
    EateryOpenHoursVO,
    EateryImageVO,
    OwnerVO
)

def get_user_entity_data():
    response = requests.get("http://users-api:8000/api/users/all/")
    content = json.loads(response.content)
    print("OWNER - USER CONTENT",content)
    for user in content["users"]:
        OwnerVO.objects.update_or_create(
            import_href=user["href"],
            defaults = {
                "username": user["username"],
                "email": user["email"],
                "phone": user["phone"],
                "first_name": user["first_name"],
                "last_name": user["last_name"]
            }
        )


def get_eatery_entity_data():
    response = requests.get("http://eateries-api:8000/api/eateries/")
    content = json.loads(response.content)
    # print("This is CONTENT;", content)
    for eatery in content["eateries"]:
        EateryVO.objects.update_or_create(
            import_href=eatery["href"],
            defaults={
                "eatery_name": eatery["eatery_name"],
                "email": eatery["email"],
                "phone": eatery["phone"],
                "website": eatery["website"],
                "yelp_id": eatery["yelp_id"],
                "review_count": eatery["review_count"],
                "average_rating": eatery["average_rating"],
                "price": eatery["price"],
                "from_yelp": eatery["from_yelp"],
                "location_address1": eatery["location"]["address1"],
                "location_address2": eatery["location"]["address2"],
                "location_address3": eatery["location"]["address3"],
                "location_city": eatery["location"]["city"],
                "location_state": eatery["location"]["state"],
                "location_zip": eatery["location"]["zip_code"],
                "location_country": eatery["location"]["country"],
                "latitude": eatery["latitude"],
                "longitude": eatery["longitude"],
            },
        )
        eateryvo_obj = EateryVO.objects.get(import_href=eatery["href"])

        # POLLING EATERYTAG MODEL
        for tag in eatery["tags"]:
            EateryTagVO.objects.update_or_create(
                import_href=tag["href"],
                defaults={"tag_name": tag["tag_name"], "eatery": eateryvo_obj},
            )

        # POLLING EATERYCATEGORY MODEL
        for category in eatery["categories"]:
            EateryCategoryVO.objects.update_or_create(
                import_href=category["href"],
                defaults={
                    "alias": category["alias"],
                    "title": category["title"],
                    "eatery": eateryvo_obj,
                },
            )

        # POLLING EATERYOPENHOURS MODEL
        for openhours_one in eatery["open_hours"]:
            EateryOpenHoursVO.objects.update_or_create(
                import_href=openhours_one["href"],
                defaults={
                    "weekday": openhours_one["weekday"],
                    "start_time": openhours_one["start_time"],
                    "end_time": openhours_one["end_time"],
                    "eatery": eateryvo_obj,
                },
            )

        # POLLING EATERYIMAGE MODEL
        for eatery_image in eatery["eatery_images"]:
            EateryImageVO.objects.update_or_create(
                import_href=eatery_image["href"],
                defaults={
                    "image_url": eatery_image["image_url"],
                    "eatery": eateryvo_obj,
                },
            )


def poll():
    while True:
        print("Service poller polling for data")
        try:
            get_eatery_entity_data()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)
        try:
            get_user_entity_data()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(10)


if __name__ == "__main__":
    poll()
