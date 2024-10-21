from django.contrib import admin

from .models import Image, Place


class ImageLine(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageLine]
