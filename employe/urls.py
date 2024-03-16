from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addEmpl", views.addEmpl, name="addEmpl"),
    path("storeEmpl", views.storeEmpl, name="storeEmpl"),
    path("showEmpl/<int:id>", views.showEmpl,name="showEmpl"),
    path("updateEmpl/<int:id>", views.updateEmpl,name="updateEmpl"),
    path("deleteEmpl/<int:id>", views.deleteEmpl,name="deleteEmpl"),
]