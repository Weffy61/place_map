from django.contrib import admin
from django.urls import path, include
from .views import show_start_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_start_page),
    path('places/', include('places.urls', namespace='places')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
