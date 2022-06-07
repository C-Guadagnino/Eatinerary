from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Foodie, Owner, EateryVO, User


@admin.register(Foodie)
class FoodieAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryVO)
class EateryVOAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
