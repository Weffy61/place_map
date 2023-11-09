from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    class Meta:
        ordering = ['pk']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey('Place',
                              on_delete=models.SET_NULL,
                              related_name='images',
                              verbose_name='Место')
    number = models.PositiveIntegerField(verbose_name='Порядковый номер изображения', default=0)
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.number
