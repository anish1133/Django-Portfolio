from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import *


class UserHome(ListView):
    model = UserDetails  # type:ignore
    template_name = "portfolio/userdetails_list.html"
    context_object_name = "User"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["ist_time"] = timezone.now().astimezone(timezone.get_current_timezone())
        context["user1"] = UserDetails.objects.all()
        context["obj"] = SocialMediaLinks.objects.all()
        return context


class AboutView(ListView):
    model = AboutMe
    template_name = "portfolio/about.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = AboutMe.objects.all()
        return context


# class Navbar(ListView):
#     model = UserDetails  # type:ignore
#     template_name = "portfolio/nav.html"
#     context_object_name = "User"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class SocialMediaicons(DetailView):
#     model = SocialMediaLinks
#     template_name = "portfolio/userdetails_list.html"
#     context_object_name = "icons"

#     def get_object(self, queryset):
#         icons = super().get_object(queryset=queryset)
