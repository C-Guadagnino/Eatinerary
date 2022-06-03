from django.contrib import admin

# from .models import OwnerVO, EateryVO
from .models import EateryCategory, EateryLocation, EateryOpenHours, EateryAdSlot

# @admin.register(OwnerVO)
# class OwnerVOAdmin(admin.ModelAdmin):
#     pass


# @admin.register(EateryVOCategory)
# class EateryVOCategoryAdmin(admin.ModelAdmin):
#     pass


@admin.register(EateryCategory)
class EateryCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryLocation)
class EateryLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryOpenHours)
class EateryOpenHoursAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryAdSlot)
class EateryAdSlotAdmin(admin.ModelAdmin):
    pass
