from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()

    features = [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse("places:place", kwargs={"place_id": place.pk}),
            },
        }
        for place in places
    ]

    place_json = {"features": features}
    context = {"places": place_json}
    return render(request, "places/index.html", context=context)


def place(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related(), pk=place_id)
    serialize_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        },
    }
    return JsonResponse(
        serialize_place, json_dumps_params={"ensure_ascii": False, "indent": 4}
    )
