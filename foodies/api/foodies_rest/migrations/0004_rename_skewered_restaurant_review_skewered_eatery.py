# Generated by Django 4.0.3 on 2022-06-16 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodies_rest', '0003_rename_eatery_eaterycategoryvo_eatery_vo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='skewered_restaurant',
            new_name='skewered_eatery',
        ),
    ]