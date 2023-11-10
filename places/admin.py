from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import Place, PlaceImage
from adminsortable2.admin import SortableAdminMixin, SortableStackedInline


class PlaceImageInline(SortableStackedInline):
    model = PlaceImage
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview']
    ordering = ['number']
    extra = 0

    def get_preview(self, image):
        style = "max-height: 200px;"

        return format_html("<b>{}</b>",
                           mark_safe('<img src="{url}" style="{style}" />'.format(
                                   url=image.image.url, style=style
                                   )
                               )
                           )


@admin.register(Place)
class PlaceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['pk', 'title']
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['number']
    raw_id_fields = ['place']


