from django.urls import path

from . import views

app_name = 'places'

urlpatterns = [
    path('<int:place_id>/',
         views.show_place_details,
         name='place_detail')
]