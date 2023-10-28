from django.urls import path

from . import views as v

app_name = "events"
urlpatterns = [
    path("", v.index, name="index"),
    path("<int:ev_id>/", v.event_details, name="details"),
    path("add/", v.add_event, name="details"),
]
