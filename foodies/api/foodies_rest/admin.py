from django.contrib import admin
from .models import Foodie


# Register your models here.
@admin.register(Foodie)
class FoodieAdmin(admin.ModelAdmin):
    pass


