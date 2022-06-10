from django.contrib import admin
from .models import (
    Foodie,
    EateryVO,
    EateryTagVO,
    EateryCategoryVO,
    EateryOpenHoursVO,
    EateryImageVO,
    SkeweredEatery,
    Review,
    ReviewImage,
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


@admin.register(EateryImageVO)
class EateryImageVOAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryCategoryVO)
class EateryCategoryVOAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryOpenHoursVO)
class EateryOpenHoursVOAdmin(admin.ModelAdmin):
    pass

@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    pass