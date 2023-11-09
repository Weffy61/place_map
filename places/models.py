from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = HTMLField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey('Place', null=True,
                              on_delete=models.SET_NULL,
                              related_name='images',
                              verbose_name='Место')
    number = models.PositiveIntegerField(verbose_name='Порядковый номер изображения')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
