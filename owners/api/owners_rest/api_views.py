from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import EateryVO
from .encoders import EateryVOEncoder
import json


# note: don't forget that the GET all EateryVOs view should also
# return the option for GET all EateryVOs FOR A SPECIFIC OWNER


@require_http_methods(["GET", "POST"])
def get_eatery_entity_data(request):
    if request.method == "GET":
        eateries = EateryVO.objects.all()
        print(eateries)
        return JsonResponse({"eatery": eateries}, encoder=EateryVOEncoder)


@require_http_methods(["GET"])
def api_get_eateryvo(request, email):
    print("I AM INSIDE HERE EATERYVO TRUST ME THE MORE WORDS THE BETTER")
    if request.method == "GET":
        eatery = EateryVO.objects.get(email=email)
        print(eatery)
        return JsonResponse(
            {"eatery": eatery},
            encoder=EateryVOEncoder
            # safe=False
        )
