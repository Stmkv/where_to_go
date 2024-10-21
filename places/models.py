from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(
        "Краткое описание", max_length=255, blank=True, null=True
    )
    description_long = models.TextField("Длинное описание", blank=True, null=True)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self):
        return self.title
