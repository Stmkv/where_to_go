from textwrap import indent

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Place


def index(request):
    places = Place.objects.all()
    place_json = {"type": "FeatureCollection", "features": []}

    for place in places:
        place_json["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude],
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": "./static/places/moscow_legends.json",
                },
            },
        )
    context = {"places": place_json}
    return render(request, "places/index.html", context=context)


def place(request, post_id):
    place = get_object_or_404(Place, pk=post_id)
    about_place = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "discription_short": place.description_short,
        "discription_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        },
    }
    return JsonResponse(
        about_place, json_dumps_params={"ensure_ascii": False, "indent": 4}
    )
