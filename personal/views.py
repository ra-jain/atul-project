from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate

# Create your views here.


def home_screen_view(request):
    user = request.user
    # if user.is_authenticated:
    #     return redirect("app")

    return render(request, "personal/home.html", {})
