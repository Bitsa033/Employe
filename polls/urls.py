from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addEmpl", views.addEmpl, name="addEmpl"),
    path("show/<int:id>", views.show),
]