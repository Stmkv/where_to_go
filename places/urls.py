from django.urls import path

from places import views

app_name = "places"

urlpatterns = [
    path("", views.index, name="index"),
    path("place/<int:place_id>/", views.place, name="place"),
]
