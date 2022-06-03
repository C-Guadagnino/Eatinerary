from django.db import models

# Create your models here.


# class OwnerVO(models.Model):
#     username = models.CharField(max_length=200)
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     phone = models.CharField(max_length=20)


class EateryVO(models.Model):
    import_href = models.CharField(max_length=200)
    # design choice decision to discuss with CuisineCoders:
    # our app will only display eateries that are claimed by an owner.
    # there cannot be an eatery that is unclaimed by an owner.
    # JK!!!! we decided that our app will display eateries from yelp even BEFORE an owner claims them
    owner = models.ForeignKey(
        "OwnerVO",
        related_name="eateries",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    eatery_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    location = models.OneToOneField(
        "EateryLocation", related_name="eatery", on_delete=models.CASCADE
    )
    website = models.URLField(max_length=200)
    yelp_id = models.CharField(max_length=200)
    # what was href for???
    href = models.URLField(max_length=200)
    review_count = models.PositiveSmallIntegerField()
    average_rating = models.FloatField()
    # "$$"
    price = models.CharField(max_length=4)
    # should this go in the EateryVO model or
    # tag = models.ManyToManyField("TagVO")
    categories = models.ManyToManyField("EateryCategory", related_name="categories")


# Do we need to bring over the Tag model as TagVO in this microservice?
# this should become more clear once we're building the React app
# class TagVO(models.Model):
#     import_href = models.CharField(max_length=200)
#     # ???
#     eatery_id = models.PositiveSmallIntegerField()
#     # more details in ManyToManyField
#     tag = models.CharField(max_length=200, unique=True)


class EateryCategory(models.Model):
    alias = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

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
    # placeholder until we have a working EateryVO model
    # eatery = models.ForeignKey("EateryVO", related_name="openhours", on_delete=models.CASCADE)
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
    # eatery = models.ForeignKey("EateryVO", related_name="images", on_delete=models.CASCADE)


class EateryAdSlot(models.Model):
    # eatery = models.ForeignKey("EateryVO", related_name="adslots", on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    # def __unicode__(self):
    #     return "%s - %s" % (
    #         self.start_datetime,
    #         self.end_datetime,
    #     )

    def __str__(self):
        return "%s - %s" % (
            self.start_datetime,
            self.end_datetime,
        )
