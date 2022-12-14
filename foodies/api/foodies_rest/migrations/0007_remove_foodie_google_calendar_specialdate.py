# Generated by Django 4.0.3 on 2022-06-19 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("foodies_rest", "0006_remove_eaterycategoryvo_eatery_vo_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="foodie",
            name="google_calendar",
        ),
        migrations.CreateModel(
            name="SpecialDate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("special_date", models.DateTimeField()),
                (
                    "occasion",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("has_passed", models.BooleanField(default=False)),
                ("repeats", models.BooleanField(default=False)),
                (
                    "frequency",
                    models.CharField(
                        blank=True,
                        choices=[("Monthly", "Monthly"), ("Yearly", "Yearly")],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "foodie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="special_dates",
                        to="foodies_rest.foodie",
                    ),
                ),
            ],
        ),
    ]
