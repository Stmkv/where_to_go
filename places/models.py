from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Заголовок", max_length=255, unique=True)
    short_description = models.TextField("Краткое описание", blank=True, null=False)
    long_description = HTMLField("Длинное описание", blank=True, null=False)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    class Meta:
        ordering = ["title"]
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Достопримечательность",
    )
    image = models.ImageField("Фото", upload_to="images/")
    number_image = models.IntegerField("Номер картинки", default=0, db_index=True)

    class Meta:
        ordering = ["number_image"]
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"

    def __str__(self):
        return f"{self.number_image}. {self.place.title}"
