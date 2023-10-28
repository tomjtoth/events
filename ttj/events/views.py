from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from . models import Event


def index(request):
    return HttpResponse(
        loader.get_template("events/index.html").render({
            "events": Event.objects.order_by("-datetime")[:5],
        }, request)
    )


def event_details(req, ev_id):
    # this cannot be merged below
    ev = get_object_or_404(Event, pk=ev_id)

    return HttpResponse(
        loader.get_template("events/details.html").render({
            "event": ev,
        }, req)
    )


def add_event(req):
    pass
