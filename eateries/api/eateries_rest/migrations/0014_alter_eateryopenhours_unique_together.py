# Generated by Django 4.0.3 on 2022-06-11 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eateries_rest", "0013_alter_yelpresult_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="eateryopenhours",
            unique_together={("weekday", "start_time", "end_time", "eatery")},
        ),
    ]
