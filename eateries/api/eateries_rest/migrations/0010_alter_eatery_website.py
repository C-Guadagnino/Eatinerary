# Generated by Django 4.0.3 on 2022-06-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eateries_rest', '0009_eatery_latitude_eatery_longitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatery',
            name='website',
            field=models.URLField(),
        ),
    ]