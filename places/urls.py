from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('<int:place_id>/',
         views.place_detail,
         name='place_detail')
]