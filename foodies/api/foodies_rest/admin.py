from django.contrib import admin
from .models import (
    Foodie,
    EateryVO,
    EateryTagVO,
    SkeweredEatery,
    Review
    )


# Register your models here.
@admin.register(Foodie)
class FoodieAdmin(admin.ModelAdmin):
    pass

@admin.register(EateryVO)
class EateryVOAdmin(admin.ModelAdmin):
    pass

@admin.register(SkeweredEatery)
class SkeweredEateryAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(EateryTagVO)
class EateryTagVOAdmin(admin.ModelAdmin):
    pass



