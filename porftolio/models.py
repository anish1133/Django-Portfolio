from django.db import models
from ckeditor.fields import RichTextField


class UserDetails(models.Model):
    intro = models.CharField(max_length=30, blank=True, verbose_name="Introduction")
    name = models.CharField(max_length=50)
    bio = models.textField(default="", blank=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    resume_link = models.URLField(blank=True, null=True)
    hire_me = models.CharField(max_length=255, default="Hire Me")

    class Meta:
        verbose_name_plural = "Heros Sec"

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    title_2 = models.CharField(max_length=100, blank=True, null=True)
    description_one = RichTextField(blank=True, null=True)
    about_avatar = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Google Drive Image Id"
    )

    class Meta:
        verbose_name_plural = "About Me Section"

    def __str__(self):
        return self.title


class ServicesOffred(models.Model):
    icon_image = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Google Drive Image Id"
    )
    service_name = models.CharField(max_length=40, blank=True, null=True)
    shadow_icon = models.CharField(max_length=40, blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Services Section"
