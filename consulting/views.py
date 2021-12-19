from msilib.schema import ListView

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegisterForm

from consulting.models import Consulting
from .forms import RegisterForm

from django.contrib import messages


# def register_consulting():
#     register_form = RegisterForm()


#     context = {
#         "form": register_form
#     }
#     return context

def add_to_db(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }

    if register_form.is_valid():
        name = register_form.cleaned_data["name"]
        email = register_form.cleaned_data["email"]
        tel = register_form.cleaned_data["tel"]
        add = register_form.cleaned_data["add"]

        Consulting.objects.create(name=name, email=email, tel=tel, add=add)

        register_form = RegisterForm()

        context = {
            "form": register_form
        }

        return render(request, "home_page.html", context)

    else:
        messages.error(request, "Error")
        return render(request, "home_page.html", context)
