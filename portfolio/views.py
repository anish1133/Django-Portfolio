from django.views.generic import ListView
from . import models
from django.utils import timezone


class UserHome(ListView):
    """Here all the UserHome class definition is done"""

    model = models.UserDetails
    context_object_name = "User"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        utc_time = timezone.now()
        ist_time = utc_time.astimezone(timezone.get_current_timezone())
        context["ist_time"] = ist_time
        return context
