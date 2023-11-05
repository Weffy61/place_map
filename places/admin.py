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

    def get_preview(self, obj):
        width = obj.image.width
        height = obj.image.height
        max_height = 200

        resize_width = (width / height) * max_height

        return format_html("<b>{}</b>",
                           mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
                                   url=obj.image.url,
                                   width=int(resize_width),
                                   height=max_height,
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


