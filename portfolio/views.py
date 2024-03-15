from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View, FormView
from django.utils import timezone
from .models import *
from . import forms
from django.shortcuts import render


class UserHome(ListView):
    model = UserDetails  # type:ignore
    template_name = "portfolio/userdetails_list.html"
    context_object_name = "User"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["ist_time"] = timezone.now().astimezone(
            timezone.get_current_timezone()
        )  # type:ignore
        context["user1"] = UserDetails.objects.all()
        context["obj"] = SocialMediaLinks.objects.all()
        return context


class AboutView(ListView):
    model = AboutMe
    template_name = "portfolio/about.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SendMessage(FormView):
    template_name = "portfolio/contact.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        Subject = form.cleaned_data["Subject"]
        message = form.cleaned_data["message"]

        print(f"Name: {name}, Email: {email}, Subject: {Subject}, Message: {message}")
        form.save()

        return super().form_valid(form)


class Skillsection(ListView):
    model = LanguagesSkills
    template_name = "portfolio/skills.html"
    context_object_name = "skills"

    def get_context_data(self, **kwargs):
        skill = LanguagesSkills.objects.all()
        context = {"skill": skill}
        return context


class ShowProject(ListView):
    model = Project
    template_name = "portfolio/projects.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Projects"] = Project.objects.all()
        context["all_photos"] = ProjectPhotos.objects.all()
        return context
