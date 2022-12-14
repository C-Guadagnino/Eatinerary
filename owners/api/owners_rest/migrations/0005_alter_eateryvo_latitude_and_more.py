# Generated by Django 4.0.3 on 2022-06-11 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "owners_rest",
            "0004_alter_eateryvo_eatery_name_alter_eateryvo_email_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="eateryvo",
            name="latitude",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_address1",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_address2",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_address3",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_country",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_state",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="location_zip",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="longitude",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="eateryvo",
            name="price",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
