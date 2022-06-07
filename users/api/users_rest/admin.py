from django.contrib import admin
from .models import Foodie, Owner, EateryVO


@admin.register(Foodie)
class FoodieAdmin(admin.ModelAdmin):
    pass


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryVO)
class EateryVOAdmin(admin.ModelAdmin):
    pass
