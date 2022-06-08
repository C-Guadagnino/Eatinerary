from django.db import models
from django.urls import reverse

# Create your models here.
class Eatery(models.Model):
    eatery_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    location = models.OneToOneField(
        "EateryLocation", related_name="eatery", on_delete=models.CASCADE
    )
    website = models.URLField(max_length=200, unique=True)
    # we might not need this, but keep it in here for convenience for now since yelp API will provide it
    yelp_id = models.CharField(max_length=200, unique=True)
    # what was href for??? Need to refresh memory
    # href = models.URLField(max_length=200, unique=True)
    review_count = models.PositiveSmallIntegerField(default=0)
    average_rating = models.FloatField()
    # "$$"
    price = models.CharField(max_length=4)
    # should the tag attribute go in the Eatery model??? or eatery = ManyToManyField to Eatery model within Tag model???
    tags = models.ManyToManyField("Tag", related_name="tags")
    categories = models.ManyToManyField("EateryCategory", related_name="categories")
    #open_hours has a foreign key to eatery and will be accessible on requests
    #eatery_image has a foreign key to eatery and will be accessible on requests
    

    def get_api_url(self):
        return reverse("api_eatery", kwargs={"pk": self.pk})


# class YelpSearchTerm(models.Model):
#     term = models.CharField(max_length=50)

# #business data
# class YelpResult(models.Model):
#     term = models.ForeignKey(
#         YelpSearchTerm,
#         on_delete=models.CASCADE,
#         related_name="results"
#     )


class Tag(models.Model):
    tag_name = models.CharField(max_length=40)
    # eatery = models.ManyToManyField("Eatery", related_name="tags")

    def __str__(self):
        return self.tag_name


class EateryCategory(models.Model):
    alias = models.CharField(max_length=200)
    title = models.CharField(max_length=200, unique=True)
    # should this eatery attribute live inside the EateryCategory model or
    # should the categories attribute live inside the Eatery model?????????????????
    # eatery = models.ManyToManyField("Eatery", related_name="categories")

    def __str__(self):
        return self.alias + " " + self.title


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

# NEEDS REVIEW BASED ON CURTIS' FEEDBACK
class EateryLocation(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, blank=True)
    address3 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, choices=STATES)
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200, default="USA")

    def get_api_url(self):
        return reverse("api_location", kwargs={"pk": self.pk})

    class Meta:
        unique_together = (
            "address1",
            "address2",
            "address3",
            "city",
            "state",
            "zip",
            "country",
        )

    def __str__(self):
        return (
            self.address1
            + " "
            + self.city
            + ", "
            + self.state
            + " "
            + self.zip
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

    class Meta:
        ordering = ("weekday", "start_time")
        unique_together = ("weekday", "start_time", "end_time")

    # def __unicode__(self):
    #     return "%s: %s - %s" % (
    #         self.get_weekday_display(),
    #         self.start_time,
    #         self.end_time,
    #     )

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
