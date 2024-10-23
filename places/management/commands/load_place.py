import logging

import requests
from django.core.exceptions import MultipleObjectsReturned
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place

logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    help = "load_json_about_place_in_database"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_url",
            type=str,
        )

    def handle(self, *args, **options):
        json_url = options["json_url"]
        response = requests.get(json_url)
        response.raise_for_status()
        decoded_response = response.json()
        try:
            place, create = Place.objects.get_or_create(
                title=decoded_response["title"],
                short_description=decoded_response["description_short"],
                long_description=decoded_response["description_long"],
                longitude=decoded_response["coordinates"]["lng"],
                latitude=decoded_response["coordinates"]["lat"],
            )
        except MultipleObjectsReturned:
            logging.info("Такое место уже есть в базе")

        for num, url in enumerate(decoded_response["imgs"], start=1):
            response = requests.get(url)
            response.raise_for_status()
            filename = f"{num}. {decoded_response['description_short']}.jpg"
            Image.objects.create(
                place=place,
                image=ContentFile(response.content, filename),
                number_image=num,
            )
