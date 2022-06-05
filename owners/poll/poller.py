import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owners_project.settings")
django.setup()

from owners_rest.models import EateryVO
# Import models from service_rest, here.
# from service_rest.models import Something
def get_eatery_entity_data():
    response = requests.get("http://eateries-api:8000/api/eateries/")
    content = json.loads(response.content)
    print("This is CONTENT;", content)
    for eatery in content["eateries"]:
        EateryVO.objects.update_or_create(
            email=eatery["email"],
            defaults={
                "email": eatery["email"],
                "phone": eatery["phone"],
                "href": eatery["href"], 
                "review_count": eatery["review_count"],
                "average_rating": eatery["average_rating"],
                "price": eatery["price"],
                "eatery_name": eatery["eatery_name"]
            },
        )


def poll():
    while True:
        print('Service poller polling for data')
        try:
            get_eatery_entity_data()
        except Exception as e:
            print(e, file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()