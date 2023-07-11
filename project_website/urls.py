
from django.urls import path
from . import views

urlpatterns = [
    path("", views.send_to_home),
    path("home/", views.home),
    path("join_now/", views.join_now)
]