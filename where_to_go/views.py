from django.shortcuts import render
from places.models import Place
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
