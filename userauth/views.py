# accounts/views.py
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from userauth.forms import AccountAuthenticationForm, RegistrationForm

# sign-up
def registration_view(request):

    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect("blog")

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "userauth/register.html", context)

# login


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("app")

    if request.POST:
        form = AccountAuthenticationForm(request. POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('blog')

    else:  # GET Request for HTML
        form = AccountAuthenticationForm()

        context['login_form'] = form
        return render(request, 'userauth/login.html', context)
