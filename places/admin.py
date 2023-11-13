from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin, SortableStackedInline

from .models import Place, PlaceImage


IMAGE_MAX_HEIGHT = 200
IMAGE_MAX_WIDTH = 200


class PlaceImageInline(SortableStackedInline):
    model = PlaceImage
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview']
    ordering = ['number']
    extra = 0

    def get_preview(self, image):
        global IMAGE_MAX_HEIGHT
        global IMAGE_MAX_WIDTH
        return format_html('<img src="{}" style="max-height: {}px; max-width: {}px;" />',
                           image.image.url, IMAGE_MAX_HEIGHT, IMAGE_MAX_WIDTH)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['pk', 'title']
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['number']
    raw_id_fields = ['place']


