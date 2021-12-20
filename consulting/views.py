from msilib.schema import ListView

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegisterForm

from consulting.models import Consulting
from .forms import RegisterForm
import re

from django.contrib import messages


# def register_consulting():
#     register_form = RegisterForm()


#     context = {
#         "form": register_form
#     }
#     return context

def consulting_form(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }

    if register_form.is_valid():
        name = register_form.cleaned_data["name"]
        email = register_form.cleaned_data["email"]
        tel = register_form.cleaned_data["tel"]
        add = register_form.cleaned_data["add"]

        Consulting.objects.create(name=name, email=email, tel=tel, add=add).save()

        register_form = RegisterForm()

        context = {
            "form": register_form
        }

        return render(request, "home_page.html", context)

    else:
        return render(request, "home_page.html", context,status=406)
