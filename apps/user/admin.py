from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.user.models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ("id", "name", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", "name")}), 
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )