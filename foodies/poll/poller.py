import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodies_project.settings")
django.setup()

from foodies_rest.models import EateryVO, EateryTagVO


def get_eatery_entity_data():
    response = requests.get("http://eateries-api:8000/api/eateries/")
    content = json.loads(response.content)
    print("This is CONTENT;", content)
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
                "location_address1": eatery["location"]["address1"],
                "location_address2": eatery["location"]["address2"],
                "location_address3": eatery["location"]["address3"],
                "location_city": eatery["location"]["city"],
                "location_state": eatery["location"]["state"],
                "location_zip": eatery["location"]["zip"],
                "location_country": eatery["location"]["country"],
                # "eatery_open_hours": eatery["eatery_open_hours"],
                # "tag": eatery["tag"],
                # "categories": eatery["categories"]
            },
        )
        eateryvo_obj = EateryVO.objects.get(import_href=eatery["href"])
        print("eateryvo_obj", eateryvo_obj)
        for tag in eatery["tags"]:
            print("tag", tag)
            print("eatery[href]", eatery["href"])
            print("tag[tag_name]", tag["tag_name"])
            EateryTagVO.objects.update_or_create(
                import_href=tag["href"],
                defaults={"tag_name": tag["tag_name"], "eatery": eateryvo_obj},
            )


def poll():
    while True:
        print("Service poller polling for data")
        try:
            get_eatery_entity_data()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(5)


if __name__ == "__main__":
    poll()
