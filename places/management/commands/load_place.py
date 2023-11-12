import os
import time
from typing import NamedTuple

from django.core.management import BaseCommand
from django.utils.safestring import mark_safe
from django.core.files.base import ContentFile
import requests

from places.models import Place, PlaceImage


class Details(NamedTuple):
    title: str
    short_description: str
    long_description: str
    lat: float
    lng: float
    images: list


def parse_place(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        place = response.json()
        place_details = Details(title=place['title'],
                                short_description=place['description_short'],
                                long_description=place['description_long'],
                                lat=place['coordinates']['lat'],
                                lng=place['coordinates']['lng'],
                                images=place['imgs']
                                )

        return place_details
    except (requests.exceptions.HTTPError, requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError, KeyError) as ex:
        print(f'Не удалось спарсить локацию, так как {ex}')


def create_place(place_details):
    place, created = Place.objects.get_or_create(title=place_details.title,
                                                 defaults=
                                                 {'short_description': place_details.short_description,
                                                  'long_description': mark_safe(place_details.long_description),
                                                  'lat': place_details.lat,
                                                  'lon': place_details.lng
                                                  })

    for count, image_link in enumerate(place_details.images, start=1):
        try:
            response = requests.get(image_link)
            response.raise_for_status()
            place_image = PlaceImage.objects.create(place=place,
                                                    number=count,
                                                    image=ContentFile(
                                                        response.content,
                                                        name=os.path.basename(image_link)))
        except (requests.exceptions.HTTPError, requests.exceptions.MissingSchema,
                requests.exceptions.ConnectionError) as ex:
            print(f'Изображение {os.path.basename(image_link)} недоступно, так как {ex}')
            time.sleep(5)
            continue
    print(f'Локация "{place.title}" успешно добавлена')


def main(json_url):
    place_details = parse_place(json_url)
    create_place(place_details)


class Command(BaseCommand):
    help = 'Команда для записи JSON файлов в бд'

    def add_arguments(self, parser):
        parser.add_argument('json_url', help='Link to JSON file')

    def handle(self, *args, **options):
        json_url = options['json_url']
        main(json_url)
