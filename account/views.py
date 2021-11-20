from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('/')


def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        email = login_form.cleaned_data.get("email")
        password = login_form.cleaned_data.get("password")
        username = User.objects.get(email=email.lower())
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error("email", 'مشخصات وارد شده صحیح نیست')

    context = {
        "form": login_form
    }
    return render(request, "account/login.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect("/")

    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get("user_name")
        first_name = register_form.cleaned_data.get("first_name")
        last_name = register_form.cleaned_data.get("last_name")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")

        User.objects.create_user(username=user_name, email=email, first_name=first_name, last_name=last_name,
                                 password=password)
        return redirect("/login/")

    context = {
        "form": register_form
    }
    return render(request, "account/register.html", context)
