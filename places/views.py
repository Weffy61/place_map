from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def show_start_page(request):
    places = Place.objects.all()
    geojson_feature = [{
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.pk,
                "detailsUrl": reverse('places:place_detail', args=[place.pk])
            }
        } for place in places]

    geojson = {
        "type": "FeatureCollection",
        "features": geojson_feature
    }

    data = {
        "geojson": geojson
    }
    return render(request, 'index.html', context=data)


def show_place_details(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('images'),
                              pk=place_id)
    place_images = place.images.all().order_by('number')
    image_paths = [place_image.image.url for place_image in place_images]

    place_details = {'title': place.title,
                     'imgs': image_paths,
                     'description_short': place.short_description,
                     'description_long': place.long_description,
                     'coordinates': {
                         'lng': place.lon,
                         'lat': place.lat
                     }
                     }
    return JsonResponse(place_details,
                        json_dumps_params={"ensure_ascii": False, 'indent': 2},
                        safe=False,
                        content_type="application/json; charset=utf-8")
