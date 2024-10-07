from django.urls import path

from . import views

urlpatterns = [
    path("csv", views.upload_csv, name="csv"),
]
