from django.contrib import admin
from .models import (
    Eatery,
    EateryCategory,
    EateryLocation,
    EateryOpenHours,
    EateryImage,
    EateryTag,
    YelpCategorySearchTerm,
    YelpLocationSearchTerm,
    YelpResult,
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


@admin.register(EateryTag)
class EateryTagAdmin(admin.ModelAdmin):
    pass


@admin.register(YelpCategorySearchTerm)
class YelpCategorySearchTermAdmin(admin.ModelAdmin):
    pass


@admin.register(YelpLocationSearchTerm)
class YelpLocationSearchTermAdmin(admin.ModelAdmin):
    pass


@admin.register(YelpResult)
class YelpResultAdmin(admin.ModelAdmin):
    pass
