from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import djwto.authentication as auth
import json

from .models import User, Foodie, Owner

# Create your views here.
@require_http_methods(["GET", "POST"])
def api_users(request):
    if request.method == "POST":
        try:
            content = json.loads(request.body)
            user = User.objects.create_user(
                username=content["username"],
                password=content["password"],
                email=content["email"],
                phone=content["phone"],
            )
            if content.get("is_foodie") and content["is_foodie"]:
                Foodie.objects.create(user=user)
            if content.get("is_owner") and content["is_owner"]:
                Owner.objects.create(user=user)
            return JsonResponse(
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                }
            )
        except IntegrityError:
            response = JsonResponse(
                {"detail": "Please enter a different username and email"}
            )
            response.status_code = 409
            return response


@require_http_methods(["GET"])
def api_user_token(request):
    if "jwt_access_token" in request.COOKIES:
        token = request.COOKIES["jwt_access_token"]
        if token:
            return JsonResponse({"token": token})
    response = JsonResponse({"detail": "no session"})
    response.status_code = 404
    return response


@require_http_methods(["GET"])
@auth.jwt_login_required
def api_get_current_user(request):

    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username,
        }
    )
