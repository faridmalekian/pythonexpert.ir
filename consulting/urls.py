from django.urls import path

from consulting.views import consulting_form

urlpatterns = [
    path('consulting', consulting_form),
]
