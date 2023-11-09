import os
import time
from places.models import Place, PlaceImage
from django.core.management import BaseCommand
import requests
from django.utils.safestring import mark_safe
from django.core.files.base import ContentFile


def parse_place(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        place = response.json()
        title = place['title']
        description_short = place['description_short']
        description_long = place['description_long']
        lat = place['coordinates']['lat']
        lng = place['coordinates']['lng']
        images = place['imgs']
        return title, description_short, description_long, lat, lng, images
    except (requests.exceptions.HTTPError, requests.exceptions.MissingSchema,
            requests.exceptions.ConnectionError, KeyError) as ex:
        print(f'Не удалось спарсить локацию, так как {ex}')


def create_place(title, description_short, description_long, lat, lng, images):
    place, created = Place.objects.get_or_create(title=title,
                                                 description_short=description_short,
                                                 description_long=mark_safe(description_long),
                                                 lat=lat,
                                                 lon=lng)
    for count, image_link in enumerate(images):
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
    link = json_url
    title, description_short, description_long, lat, lng, images = parse_place(link)
    create_place(title, description_short, description_long, lat, lng, images)


class Command(BaseCommand):
    help = 'Команда для записи JSON файлов в бд'

    def add_arguments(self, parser):
        parser.add_argument('json_url', help='Link to JSON file')

    def handle(self, *args, **options):
        json_url = options['json_url']
        main(json_url)
