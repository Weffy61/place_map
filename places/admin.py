from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin, SortableStackedInline

from .models import Place, PlaceImage


class PlaceImageInline(SortableStackedInline):
    model = PlaceImage
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview']
    ordering = ['number']
    extra = 0

    def get_preview(self, image):
        max_height = 200
        max_width = 200
        return format_html('<img src="{}" style="max-height: {}px; max-width: {}px;" />',
                           image.image.url, max_height, max_width)


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['pk', 'title']
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['number']
    raw_id_fields = ['place']


