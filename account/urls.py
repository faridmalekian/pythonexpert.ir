from django.urls import path
from .views import login_user,register,logout_view

urlpatterns = [
    path('login/',login_user),
    path('register/',register),
    path('logout',logout_view),
]