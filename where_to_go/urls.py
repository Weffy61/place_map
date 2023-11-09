from django.contrib import admin
from django.urls import path, include
from places.views import show_start_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_start_page),
    path('places/', include('places.urls', namespace='places')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
