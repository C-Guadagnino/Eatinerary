# Generated by Django 4.0.3 on 2022-06-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eateries_rest', '0007_yelpsearchterm_yelpresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eaterycategory',
            name='alias',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='eaterycategory',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
