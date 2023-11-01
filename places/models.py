from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места')
    description_short = models.TextField(max_length=250, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return self.title

