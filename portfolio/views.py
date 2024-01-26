from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetails


# Create your views here.
def user_detail(request):
    all_users = UserDetails.objects.all()
    print((all_users))
    return render(request, "home/home.html", context={"all_users": all_users})
