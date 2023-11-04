from django.shortcuts import render
from places.models import Place, PlaceImage


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
                "detailsUrl": "./static/json/moscow_legends.json"
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
