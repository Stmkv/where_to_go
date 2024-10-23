from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place

MAX_WIDTH_IMAGE = 150
MAX_HEIGHT_IMAGE = 150


class ImageLine(SortableStackedInline):
    model = Image
    readonly_fields = ["get_preview"]
    fields = [
        "image",
        "number_image",
        "get_preview",
    ]

    def get_preview(self, obj):
        return format_html(
            '<img src="{}" style="max-width: {}px; max-height: {}px;"/>',
            obj.image.url,
            MAX_WIDTH_IMAGE,
            MAX_HEIGHT_IMAGE,
        )

    get_preview.short_description = "Картинка"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageLine]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("number_image", "place")
    raw_id_fields = ["place"]
