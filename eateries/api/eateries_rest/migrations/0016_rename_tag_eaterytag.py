# Generated by Django 4.0.3 on 2022-06-18 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eateries_rest', '0015_alter_eatery_yelp_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tag',
            new_name='EateryTag',
        ),
    ]