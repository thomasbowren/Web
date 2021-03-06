from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thomas", views.thomas, name="thomas"),
    path("<str:name>", views.greet, name="greet")
]
