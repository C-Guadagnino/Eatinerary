from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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


# class SkeweredEatery(models.Model):
#     eatery = models.ForeignKey(
#     EateryVO,
#     related_name="skewered_eatery",
#     on_delete=models.CASCADE,
#     )
#     foodie = models.ForeignKey(
#         Foodie,
#         related_name="foodie",
#         on_delete=models.CASCADE,
#         blank=True #needs review!
#     )
#     created_DateTime = models.DateTimeField(auto_now_add=True)
#     updated_DateTime = models.DateTimeField(auto_now=True)
#     has_visited = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#     notes = models.TextField()

#     def __str__(self):
#         return self.foodie + " " + self.notes # + self.eatery


# class ImageVO(models.Model):
#     image_url = models.URLField(unique=True)
#     image_url2 = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, unique=True)


# class Review(models.Model):
#     title = models.CharField(max_length=100)
#     rating = models.PositiveSmallIntegerField(
#         validators=[
#             MaxValueValidator(5),
#             MinValueValidator(1),
#         ]
#     )
#     created_DateTime = models.DateTimeField(auto_now_add=True)
#     description = models.TextField()
#     skewered_restaurant = models.OneToOneField(
#         SkeweredEatery,
#         on_delete=models.CASCADE,
#         primary_key=True
#     )
#     image = models.ForeignKey(
#         ImageVO,
#         related_name = "image",
#         on_delete=models.CASCADE,
#         blank=True
#     )

#     def __str__(self):
#         restaurant = str(self.skewered_restaurant)
#         return self.title + " for " + restaurant
