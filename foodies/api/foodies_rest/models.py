from django.urls import reverse
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class EateryTagVO(models.Model):
    import_href = models.CharField(max_length=200)
    tag_name = models.CharField(max_length=40)
    eatery_vo = models.ManyToManyField("EateryVO", related_name="tagsvo")

    def __str__(self):
        return "Tag #" + self.tag_name


class EateryCategoryVO(models.Model):
    import_href = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    eatery_vo = models.ManyToManyField("EateryVO", related_name="categoriesvo")

    def __str__(self):
        return "Category " + self.alias


class EateryImageVO(models.Model):
    import_href = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    # image_url2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, unique=True)
    eatery_vo = models.ForeignKey(
        "EateryVO", related_name="eateryimagesvo", on_delete=models.CASCADE
    )

    def __str__(self):
        return "Image " + self.image_url + " for Eatery: " + self.eatery_vo.eatery_name


class EateryOpenHoursVO(models.Model):
    import_href = models.CharField(max_length=200)
    weekday = models.CharField(max_length=200)
    start_time = models.TimeField()
    end_time = models.TimeField()
    eatery_vo = models.ForeignKey(
        "EateryVO", related_name="allopenhoursvo", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            "Open Hours for Eatery "
            + self.eatery_vo.eatery_name
            + " on "
            + self.weekday
        )


class Foodie(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    google_calendar = models.URLField(blank=True, null=True)

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

    def __str__(self):
        return self.eatery_name


class SkeweredEatery(models.Model):
    eatery_vo = models.ForeignKey(
        EateryVO,
        related_name="skewered_eateries",
        on_delete=models.CASCADE,
    )
    foodie = models.ForeignKey(
        Foodie,
        related_name="skewered_eateries",
        on_delete=models.CASCADE,
    )
    created_DateTime = models.DateTimeField(auto_now_add=True)
    updated_DateTime = models.DateTimeField(auto_now=True)
    has_visited = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    notes = models.TextField()

    def __str__(self):
        return self.eatery_vo.eatery_name


class Review(models.Model):
    title = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    created_DateTime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    eatery_vo = models.ForeignKey(
        EateryVO,
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    skewered_eatery = models.OneToOneField(
        SkeweredEatery,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        eatery = str(self.skewered_eatery)
        return self.title + " for " + eatery


class ReviewImage(models.Model):
    image_url = models.URLField(unique=True)
    review = models.ForeignKey(
        "Review", related_name="review_images", on_delete=models.CASCADE
    )

    def get_api_url(self):
        return reverse("api_eatery_image", kwargs={"pk": self.pk})
