from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    description_short = models.TextField(max_length=250, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey('Place', null=True, on_delete=models.SET_NULL, related_name='images')
    number = models.PositiveIntegerField(verbose_name='Порядковый номер изображения')
    title = models.CharField(max_length=200, verbose_name='Название изображения')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return self.title
