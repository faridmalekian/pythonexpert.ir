from django.urls import path

from consulting.views import add_to_db

urlpatterns = [
    path('consulting', add_to_db),
]
