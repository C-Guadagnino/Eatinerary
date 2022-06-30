from django.db import models
from django.urls import reverse



class Eatery(models.Model):
    eatery_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200)
    location = models.OneToOneField(
        "EateryLocation", related_name="eatery", on_delete=models.CASCADE
    )
    website = models.URLField(max_length=500)
    yelp_id = models.CharField(max_length=200, blank=True, null=True)
    review_count = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField()
    price = models.CharField(max_length=4, null=True, blank=True)
    tags = models.ManyToManyField("EateryTag", related_name="tags")
    categories = models.ManyToManyField(
        "EateryCategory", related_name="categories"
    )
    from_yelp = models.BooleanField(default=False)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def get_api_url(self):
        return reverse("api_eatery", kwargs={"pk": self.pk})

    def __str__(self):
        categories_str = ""

        for i, category in enumerate(self.categories.all()):
            if i == 0:
                categories_str = categories_str + category.alias
            else:
                categories_str = categories_str + ", " + category.alias

        return (
            self.eatery_name
            + " for <"
            + categories_str
            + "> in "
            + str(self.location.city)
            + ", "
            + str(self.location.state)
        )



class YelpCategorySearchTerm(models.Model):
    category_term = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_term


class YelpLocationSearchTerm(models.Model):
    location_term = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.location_term


class YelpResult(models.Model):
    category_term = models.ForeignKey(
        YelpCategorySearchTerm,
        on_delete=models.CASCADE,
        related_name="results",
    )
    location_term = models.ForeignKey(
        YelpLocationSearchTerm,
        on_delete=models.CASCADE,
        related_name="results",
    )
    eatery = models.ForeignKey(
        "Eatery", related_name="eatery_yelpresults", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = (
            "category_term",
            "location_term",
            "eatery",
        )

    def __str__(self):
        return (
            "CATEGORY: "
            + self.category_term.category_term
            + " LOCATION: "
            + self.location_term.location_term
            + " - "
            + self.eatery.eatery_name
        )


class EateryTag(models.Model):
    tag_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.tag_name

    def get_api_url(self):
        return reverse("api_tag", kwargs={"tag_name": self.tag_name})


class EateryCategory(models.Model):
    alias = models.CharField(max_length=200, unique=True, db_index=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.alias + " " + self.title

    def get_api_url(self):
        return reverse("api_category", kwargs={"pk": self.pk})


STATES = [
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
]


class EateryLocation(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    address3 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, db_index=True)
    state = models.CharField(max_length=200, choices=STATES)
    zip_code = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default="USA")

    def get_api_url(self):
        return reverse("api_location", kwargs={"pk": self.pk})

    def __str__(self):
        return (
            self.address1
            + " "
            + self.city
            + ", "
            + self.state
            + " "
            + self.zip_code
            + ", "
            + self.country
        )


WEEKDAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]


class EateryOpenHours(models.Model):

    eatery = models.ForeignKey(
        "Eatery", related_name="open_hours", on_delete=models.CASCADE
    )
    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def get_weekday_display(self):
        return WEEKDAYS[self.weekday - 1][1]

    def get_api_url(self):
        return reverse("api_open_hours_singular", kwargs={"pk": self.pk})

    class Meta:
        ordering = ("weekday", "start_time")
        unique_together = ("weekday", "start_time", "end_time", "eatery")

    def __str__(self):
        return "%s: %s - %s" % (
            self.get_weekday_display(),
            self.start_time,
            self.end_time,
        )


class EateryImage(models.Model):
    image_url = models.TextField()
    eatery = models.ForeignKey(
        "Eatery", related_name="eatery_images", on_delete=models.CASCADE
    )

    def get_api_url(self):
        return reverse("api_eatery_image", kwargs={"pk": self.pk})
