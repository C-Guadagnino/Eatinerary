from django.contrib import admin
from .models import (
    Eatery,
    EateryCategory,
    EateryLocation,
    EateryOpenHours,
    EateryImage,
    Tag,
)


@admin.register(Eatery)
class EateryAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryCategory)
class EateryCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryLocation)
class EateryLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryOpenHours)
class EateryOpenHoursAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryImage)
class EateryImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
