from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.UserDetails)
class ItemUser(admin.ModelAdmin):
    list_display = (
        "intro",
        "name",
        "bio",
        "job_title",
        "avatar",
        "resume_link",
        "hire_me",
    )


@admin.register(models.AboutMe)
class About(admin.ModelAdmin):
    list_display = ("title", "title_2", "description_one", "about_avatar")


@admin.register(models.ServicesOffered)
class Display_Service(admin.ModelAdmin):
    list_display = ("icon_image", "service_name", "shadow_icon", "service_description")
