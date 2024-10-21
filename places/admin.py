from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from .models import Image, Place


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
            '<img src="{url}" width="150" height="150" />'.format(url=obj.image.url)
        )

    get_preview.short_description = "Картинка"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageLine]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("number_image", "place")
    raw_id_fields = ["place"]
