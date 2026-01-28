from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.landing_page.models import Features, FooterSection, HeroSection, HowItWorks, TakeTheGuessworkOutOfHairCare, TrustAndTransparency, WhyHairiSafeExists

@admin.register(HeroSection)
class HeroSectionAdmin(ModelAdmin):
    list_display = ("id", "title", "subtitle", "background_image")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "subtitle", "background_image")}),
    )

@admin.register(HowItWorks)
class HowItWorksAdmin(ModelAdmin):
    list_display = ("id", "title", "subtitle", "image")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "subtitle", "image")}),
    )

@admin.register(WhyHairiSafeExists)
class WhyHairiSafeExistsAdmin(ModelAdmin):
    list_display = ("id", "title", "subtitle", "image")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "subtitle", "image")}),
    )   

@admin.register(Features)
class FeaturesAdmin(ModelAdmin):
    list_display = ("id", "title", "icon")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "icon")}),
    )

@admin.register(TrustAndTransparency)
class TrustAndTransparencyAdmin(ModelAdmin):
    list_display = ("id", "title", "icon")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "icon")}),
    )

@admin.register(TakeTheGuessworkOutOfHairCare)
class TakeTheGuessworkOutOfHairCareAdmin(ModelAdmin):
    list_display = ("id", "title", "link")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "link")}),
    )

@admin.register(FooterSection)
class FooterSectionAdmin(ModelAdmin):
    list_display = ("id", "title", "icon", "link")
    search_fields = ("title",)
    fieldsets = (
        (None, {"fields": ("title", "icon", "link")}),
    )


