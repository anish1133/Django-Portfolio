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
        "dev_domain",
        "hire_me",
    )


@admin.register(models.AboutMe)
class About(admin.ModelAdmin):
    list_display = ("resume",)


@admin.register(models.ServicesOffered)
class Display_Service(admin.ModelAdmin):
    list_display = (
        "icon_image",
        "service_name",
        "shadow_icon",
        "service_description",
    )


@admin.register(models.LanguagesSkills)
class Skills(admin.ModelAdmin):
    list_display = (
        "EXP_CHOICES",
        "icon",
        "lang_name",
        "exp_level",
    )


@admin.register(models.Project)
class Project_View(admin.ModelAdmin):
    list_display = (
        "language_used",
        "Project_Image",
        "updated_on",
        "Project_title",
        "Project_info",
        "project_link",
        "live_link",
    )


@admin.register(models.MyContact)
class Contact(admin.ModelAdmin):
    list_display = (
        "icon",
        "contact_info",
        "social",
    )


@admin.register(models.SocialMediaLinks)
class Social(admin.ModelAdmin):
    list_display = (
        "name",
        "link",
        "social_icon",
    )
