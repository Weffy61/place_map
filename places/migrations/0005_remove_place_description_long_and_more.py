# Generated by Django 4.2.6 on 2023-11-10 01:09

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0004_alter_place_options_alter_placeimage_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="place", name="description_long",),
        migrations.RemoveField(model_name="place", name="description_short",),
        migrations.AddField(
            model_name="place",
            name="long_description",
            field=tinymce.models.HTMLField(blank=True, verbose_name="Полное описание"),
        ),
        migrations.AddField(
            model_name="place",
            name="short_description",
            field=models.TextField(blank=True, verbose_name="Краткое описание"),
        ),
        migrations.AlterField(
            model_name="placeimage",
            name="number",
            field=models.PositiveIntegerField(
                db_index=True, default=0, verbose_name="Порядковый номер изображения"
            ),
        ),
        migrations.AlterField(
            model_name="placeimage",
            name="place",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.place",
                verbose_name="Место",
            ),
        ),
    ]
