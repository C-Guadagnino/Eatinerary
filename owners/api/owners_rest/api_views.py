from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import EateryVO
from .encoders import EateryVOEncoder
import json


@require_http_methods(["GET", "PUT"])
def get_eatery_entity_data(request):
    if request.method == "GET":
        eateries = EateryVO.objects.all()
        print(eateries)
        return JsonResponse(
            {"eatery": eateries},
            encoder=EateryVOEncoder
        )
