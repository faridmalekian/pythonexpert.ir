from consulting.forms import RegisterForm
from django.shortcuts import render, redirect
from courses_category.models import Category


def home_page(request):
    categories = Category.objects.all()

    register_form = RegisterForm()
    context = {
        'categories': categories,
        'form': register_form

    }
    # context.update(register_form)
    return render(request, "home_page.html", context)
