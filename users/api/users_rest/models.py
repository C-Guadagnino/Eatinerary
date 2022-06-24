from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    phone = models.CharField(max_length=200, unique=True)
    google_calendar = models.URLField(unique=True, blank=True, null=True)

    def get_api_url(self):
        return reverse("api_users", kwargs={"pk": self.pk})


class Foodie(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="foodie",
    )


class Owner(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="owner",
    )


class EateryVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(
        "Owner", related_name="eateries", on_delete=models.CASCADE
    )
