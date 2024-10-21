from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField("Краткое описание", blank=True, null=True)
    description_long = HTMLField("Длинное описание", blank=True, null=True)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField("Фото", upload_to="images/")
    number_image = models.IntegerField("Номер картинки", default=0)

    def __str__(self):
        return f"{self.number_image}. {self.place.title}"

    class Meta:
        ordering = ["number_image"]
