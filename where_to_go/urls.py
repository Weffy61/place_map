from django.contrib import admin
from django.urls import path
from .views import show_start_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_start_page),
]
