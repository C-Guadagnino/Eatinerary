from django.contrib import admin

from .models import EateryVO, EateryAdSlot, EateryTagVO, OwnerVO


@admin.register(OwnerVO)
class OwnerVOAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryVO)
class EateryVOAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryAdSlot)
class EateryAdSlotAdmin(admin.ModelAdmin):
    pass


@admin.register(EateryTagVO)
class EateryTagVOAdmin(admin.ModelAdmin):
    pass
