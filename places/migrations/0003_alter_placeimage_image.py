# Generated by Django 4.2.6 on 2023-11-03 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0002_placeimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="placeimage",
            name="image",
            field=models.ImageField(upload_to="images/", verbose_name="Изображение"),
        ),
    ]
