from django.db import models

# Create your models here.

class EateryTagVO(models.Model):
    import_href = models.CharField(max_length=200)
    tag_name = models.CharField(max_length=40)
    eatery = models.ForeignKey(
        "EateryVO", related_name="tagsvo", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Tag #" + self.tag_name + " for Eatery: " + self.eatery.eatery_name


class EateryCategoryVO(models.Model):
    import_href = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    eatery = models.ForeignKey(
        "EateryVO", related_name="categoriesvo", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Category " + self.alias + " for Eatery: " + self.eatery.eatery_name


class EateryImageVO(models.Model):
    import_href = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    # image_url2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, unique=True)
    eatery = models.ForeignKey(
        "EateryVO", related_name="eateryimagesvo", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Image " + self.image_url + " for Eatery: " + self.eatery.eatery_name


class EateryOpenHoursVO(models.Model):
    import_href = models.CharField(max_length=200)
    weekday = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    eatery = models.ForeignKey(
        "EateryVO", related_name="allopenhoursvo", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            "Open Hours for Eatery " + self.eatery.eatery_name + " on " + self.weekday
        )

class OwnerVO(models.Model):
    import_href = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    # google_calendar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.username


class EateryVO(models.Model):
    import_href = models.CharField(max_length=200)
    eatery_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200)
    website = models.URLField(max_length=500)
    yelp_id = models.CharField(max_length=200)
    review_count = models.PositiveIntegerField(default=0)
    average_rating = models.FloatField()
    price = models.CharField(max_length=4, blank=True, null=True)
    from_yelp = models.BooleanField()
    location_address1 = models.CharField(max_length=200, blank=True, null=True)
    location_address2 = models.CharField(max_length=200, blank=True, null=True)
    location_address3 = models.CharField(max_length=200, blank=True, null=True)
    location_city = models.CharField(max_length=200, blank=True, null=True)
    location_state = models.CharField(max_length=200, blank=True, null=True)
    location_zip = models.CharField(max_length=200, blank=True, null=True)
    location_country = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    # We decided that our app will display eateries from yelp even BEFORE an owner claims them
    # Question: Can ForeignKeys take null=True, blank=True? Test this out later.
    # owner = models.ForeignKey(
    #     "OwnerVO",
    #     related_name="eateries",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )



# Brandon and Ariana believe that this AdSlot model should live in the Owners microservice,
# and NOT in the Eateris microservice because an AdSlot would not exist if an Owner didn't pay for it
class EateryAdSlot(models.Model):
    eatery = models.ForeignKey(
        "EateryVO", related_name="adslots", on_delete=models.CASCADE
    )
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
