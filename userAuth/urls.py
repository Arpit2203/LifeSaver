from django.urls import path
from . import views

urls = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    ]
