# Generated by Django 4.0.3 on 2022-06-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodies_rest', '0004_rename_skewered_restaurant_review_skewered_eatery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eaterytagvo',
            name='eatery_vo',
        ),
        migrations.AddField(
            model_name='eaterytagvo',
            name='eatery_vo',
            field=models.ManyToManyField(related_name='tagsvo', to='foodies_rest.eateryvo'),
        ),
    ]