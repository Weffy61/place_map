from django.shortcuts import get_object_or_404
from places.models import Place, PlaceImage
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse


def show_start_page(request):
    places = Place.objects.all()
    geojson_feature = []
    for place in places:

        feature = {
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
        }
        geojson_feature.append(feature)
    geojson = {
        "type": "FeatureCollection",
        "features": geojson_feature
    }

    data = {
        "geojson": geojson
    }
    return render(request, 'index.html', context=data)


def place_detail(request, place_id):
    place = get_object_or_404(Place,
                              pk=place_id)
    place_images = PlaceImage.objects.filter(place=place)
    images_path = [place_image.image.url for place_image in place_images]

    data = {'title': place.title,
            'imgs': images_path,
            'description_short': place.short_description,
            'description_long': place.long_description,
            'coordinates': {
                'lng': place.lon,
                'lat': place.lat
            }
            }
    return JsonResponse(data,
                        json_dumps_params={"ensure_ascii": False, 'indent': 2},
                        safe=False,
                        content_type="application/json; charset=utf-8")
