from typing import NamedTuple
import os
import time

from places.models import Place, PlaceImage
from django.core.management import BaseCommand
from django.utils.safestring import mark_safe
from django.core.files.base import ContentFile
import requests


def parse_place(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        place = response.json()

        Details = NamedTuple('Details', [
            ('title', str),
            ('short_description', str),
            ('long_description', str),
            ('lat', float),
            ('lng', float),
            ('images', list)
        ])

        place_details = Details(place['title'],
                                place['description_short'],
                                place['description_long'],
                                place['coordinates']['lat'],
                                place['coordinates']['lng'],
                                place['imgs']
                                )
        return place_details
    except (requests.exceptions.HTTPError, requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError, KeyError) as ex:
        print(f'Не удалось спарсить локацию, так как {ex}')


def create_place(place_details):
    place, created = Place.objects.get_or_create(title=place_details.title,
                                                 short_description=place_details.short_description,
                                                 long_description=mark_safe(place_details.long_description),
                                                 lat=place_details.lat,
                                                 lon=place_details.lng)
    for count, image_link in enumerate(place_details.images):
        try:
            response = requests.get(image_link)
            response.raise_for_status()
            place_image = PlaceImage.objects.create(place=place, number=count + 1)
            place_image.image.save(os.path.basename(image_link), ContentFile(response.content), save=True)
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
