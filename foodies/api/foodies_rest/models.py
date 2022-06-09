from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .resources import STATES


class EateryTagVO(models.Model):
    import_href = models.CharField(max_length=200)
    tag_name = models.CharField(max_length=40)
    eatery = models.ForeignKey(
        "EateryVO",
        related_name="tagsvo",
        on_delete= models.CASCADE
    )

class EateryCategoriesVO(models.Model):
    alias = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

class ImageVO(models.Model):
    image_url = models.URLField(unique=True)
    #image_url2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, unique=True)

# Create your models here.
class Foodie(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=13, unique=True)
    google_calendar = models.URLField(null=True)  # needs review

    def __str__(self):
        return self.username

class EateryVO(models.Model):
    import_href = models.CharField(max_length=200)
    eatery_name = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    website = models.URLField(max_length=200, unique=True)
    yelp_id = models.CharField(max_length=200, unique=True)
    review_count = models.PositiveSmallIntegerField(default=0)
    average_rating = models.FloatField()
    price = models.CharField(max_length=4)
    location_address1 = models.CharField(max_length=200)
    location_address2 = models.CharField(max_length=200)
    location_address3 = models.CharField(max_length=200)
    location_city = models.CharField(max_length=200)
    location_state = models.CharField(max_length=200)
    location_zip = models.CharField(max_length=200)
    location_country = models.CharField(max_length=200)
    #eatery_open_hours = models.CharField(max_length=200)
    #eatery_image = models.
    #M2M
    # tag = models.ForeignKey(
    #     EateryTagVO,
    #     related_name="foodies_tag",
    #     on_delete = models.CASCADE
    # )
    # #M2M
    # categories = models.ForeignKey(
    #     EateryCategoriesVO,
    #     related_name="foodies_categories",
    #     on_delete = models.CASCADE
    # ) 


class SkeweredEatery(models.Model):
    eatery = models.ForeignKey(
    EateryVO,
    related_name="skewered_eatery",
    on_delete=models.CASCADE,
    )
    foodie = models.ForeignKey(
        Foodie,
        related_name="foodie",
        on_delete=models.CASCADE,
        blank=True #needs review!
    )
    created_DateTime = models.DateTimeField(auto_now_add=True)
    updated_DateTime = models.DateTimeField(auto_now=True)
    has_visited = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    notes = models.TextField()

    def __str__(self):
        return self.eatery


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
    skewered_restaurant = models.OneToOneField(
        SkeweredEatery,
        on_delete=models.CASCADE,
        primary_key=True
    )
    image = models.ForeignKey(
        ImageVO,
        related_name = "image",
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        restaurant = str(self.skewered_restaurant)
        return self.title + " for " + restaurant
