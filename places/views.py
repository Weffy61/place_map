from django.shortcuts import render, get_object_or_404
from places.models import Place, PlaceImage
from django.http import JsonResponse


def place_detail(request, place_id):
    place = get_object_or_404(Place,
                              pk=place_id)
    place_images = PlaceImage.objects.filter(place=place)
    images_path = [str(place_image.image.url) for place_image in place_images]

    data = {'title': place.title,
            'imgs': images_path,
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng': place.lon,
                'lat': place.lat
            }
            }
    return JsonResponse(data,
                        json_dumps_params={"ensure_ascii": False, 'indent': 2},
                        safe=False,
                        content_type="application/json; charset=utf-8")
