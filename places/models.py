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


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Фото", upload_to="images/")
    number_image = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.number_image}. {self.place.title}"
