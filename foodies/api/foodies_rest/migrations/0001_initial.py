import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EateryVO",
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
                ("import_href", models.CharField(max_length=200)),
                ("eatery_name", models.CharField(max_length=200)),
                (
                    "email",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("phone", models.CharField(max_length=200)),
                ("website", models.URLField(max_length=500)),
                ("yelp_id", models.CharField(max_length=200)),
                ("review_count", models.PositiveIntegerField(default=0)),
                ("average_rating", models.FloatField()),
                (
                    "price",
                    models.CharField(blank=True, max_length=4, null=True),
                ),
                ("from_yelp", models.BooleanField()),
                (
                    "location_address1",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_address2",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_address3",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_city",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_state",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_zip",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "location_country",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "latitude",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "longitude",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Foodie",
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
                ("username", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=13, unique=True)),
                ("google_calendar", models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("title", models.CharField(max_length=100)),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("created_DateTime", models.DateTimeField(auto_now_add=True)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SkeweredEatery",
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
                ("created_DateTime", models.DateTimeField(auto_now_add=True)),
                ("updated_DateTime", models.DateTimeField(auto_now=True)),
                ("has_visited", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("notes", models.TextField()),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skewered_eatery",
                        to="foodies_rest.eateryvo",
                    ),
                ),
                (
                    "foodie",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="foodie",
                        to="foodies_rest.foodie",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReviewImage",
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
                ("image_url", models.URLField(unique=True)),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_images",
                        to="foodies_rest.review",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="review",
            name="skewered_restaurant",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="foodies_rest.skeweredeatery",
            ),
        ),
        migrations.CreateModel(
            name="EateryTagVO",
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
                ("import_href", models.CharField(max_length=200)),
                ("tag_name", models.CharField(max_length=40)),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tagsvo",
                        to="foodies_rest.eateryvo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EateryOpenHoursVO",
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
                ("import_href", models.CharField(max_length=200)),
                ("weekday", models.CharField(max_length=200)),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="allopenhoursvo",
                        to="foodies_rest.eateryvo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EateryImageVO",
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
                ("import_href", models.CharField(max_length=200)),
                ("image_url", models.CharField(max_length=200)),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eateryimagesvo",
                        to="foodies_rest.eateryvo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EateryCategoryVO",
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
                ("import_href", models.CharField(max_length=200)),
                ("alias", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categoriesvo",
                        to="foodies_rest.eateryvo",
                    ),
                ),
            ],
        ),
    ]
