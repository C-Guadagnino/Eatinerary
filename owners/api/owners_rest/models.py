from django.db import models

# Create your models here.

# OwnerVO

# EateryVO


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
    # eatery = models.ForeignKey("EateryVO")
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


class EateryAdSlot(models.Model):
    # eatery = models.ForeignKey("EateryVO")
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
