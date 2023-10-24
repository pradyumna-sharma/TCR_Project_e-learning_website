from django.contrib import admin
from .models import CustomUser, Course, PurchasedCourse
from django.utils.html import format_html

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'photo_display')

    def photo_display(self, obj):
        if obj.photo:
            image_url = obj.photo.url
            return format_html('<img src="{}" width="50" height="50" />', image_url)
        return "No Image"

    photo_display.short_description = 'Photo'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(PurchasedCourse)
