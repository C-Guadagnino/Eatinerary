# Generated by Django 4.0.3 on 2022-06-09 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Eatery",
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
                ("eatery_name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200, unique=True)),
                ("phone", models.CharField(max_length=200)),
                ("website", models.URLField(unique=True)),
                ("yelp_id", models.CharField(max_length=200, unique=True)),
                ("review_count", models.PositiveSmallIntegerField(default=0)),
                ("average_rating", models.FloatField()),
                ("price", models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="EateryCategory",
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
                ("alias", models.CharField(max_length=200, unique=True)),
                ("title", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("tag_name", models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="YelpCategorySearchTerm",
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
                ("category_term", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="YelpLocationSearchTerm",
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
                ("location_term", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="YelpResult",
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
                (
                    "category_terms",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="eateries_rest.yelpcategorysearchterm",
                    ),
                ),
                (
                    "location_terms",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="eateries_rest.yelplocationsearchterm",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EateryLocation",
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
                ("address1", models.CharField(max_length=200)),
                ("address2", models.CharField(blank=True, max_length=200)),
                ("address3", models.CharField(blank=True, max_length=200)),
                ("city", models.CharField(max_length=200)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AL", "Alabama"),
                            ("AK", "Alaska"),
                            ("AS", "American Samoa"),
                            ("AZ", "Arizona"),
                            ("AR", "Arkansas"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Connecticut"),
                            ("DE", "Delaware"),
                            ("DC", "District of Columbia"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("GU", "Guam"),
                            ("HI", "Hawaii"),
                            ("ID", "Idaho"),
                            ("IL", "Illinois"),
                            ("IN", "Indiana"),
                            ("IA", "Iowa"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Louisiana"),
                            ("ME", "Maine"),
                            ("MD", "Maryland"),
                            ("MA", "Massachusetts"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MS", "Mississippi"),
                            ("MO", "Missouri"),
                            ("MT", "Montana"),
                            ("NE", "Nebraska"),
                            ("NV", "Nevada"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NY", "New York"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("MP", "Northern Mariana Islands"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennsylvania"),
                            ("PR", "Puerto Rico"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennessee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VT", "Vermont"),
                            ("VI", "Virgin Islands"),
                            ("VA", "Virginia"),
                            ("WA", "Washington"),
                            ("WV", "West Virginia"),
                            ("WI", "Wisconsin"),
                            ("WY", "Wyoming"),
                        ],
                        max_length=200,
                    ),
                ),
                ("zip", models.CharField(max_length=200)),
                ("country", models.CharField(default="USA", max_length=200)),
            ],
            options={
                "unique_together": {
                    (
                        "address1",
                        "address2",
                        "address3",
                        "city",
                        "state",
                        "zip",
                        "country",
                    )
                },
            },
        ),
        migrations.CreateModel(
            name="EateryImage",
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
                ("image_url", models.TextField()),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="eatery_images",
                        to="eateries_rest.eatery",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="eatery",
            name="categories",
            field=models.ManyToManyField(
                related_name="categories", to="eateries_rest.eaterycategory"
            ),
        ),
        migrations.AddField(
            model_name="eatery",
            name="location",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eatery",
                to="eateries_rest.eaterylocation",
            ),
        ),
        migrations.AddField(
            model_name="eatery",
            name="tags",
            field=models.ManyToManyField(
                related_name="tags", to="eateries_rest.tag"
            ),
        ),
        migrations.CreateModel(
            name="EateryOpenHours",
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
                (
                    "weekday",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ]
                    ),
                ),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "eatery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="open_hours",
                        to="eateries_rest.eatery",
                    ),
                ),
            ],
            options={
                "ordering": ("weekday", "start_time"),
                "unique_together": {("weekday", "start_time", "end_time")},
            },
        ),
    ]
