from django.urls import path
from . import views as portfolio_views

app_name = "portfolio"

urlpatterns = [
    path("", portfolio_views.UserHome.as_view(), name="home"),
    path("about/", portfolio_views.AboutView.as_view(), name="about"),
    path("contact/", portfolio_views.SendMessage.as_view(), name="contact"),
    path("skills/", portfolio_views.Skillsection.as_view(), name="skills"),
]
