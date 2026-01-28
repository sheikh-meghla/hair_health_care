from django.contrib import admin

from apps.chatbot.models import HairImage

# Register your models here.
@admin.register(HairImage)
class HairImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    readonly_fields = ('created_at',)