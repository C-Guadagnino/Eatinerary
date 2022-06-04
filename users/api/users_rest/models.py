from django.db import models

# BELOW IMPORT IS FOR HAVING CUSTOM USER MODEL
# We used AbstractUser in FearlessFrontend, but we Django Docs recommend AbstractBaseUser ???
# from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import AbstractBaseUser

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# DO WE NEED THIS CUSTOM USER MODEL IN ORDER FOR THE FOODIES AND OWNERS TO BE ABLE TO SIGN UP/LOG IN???
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class User(AbstractUser):
# WHAT ATTRIBUTES DO WE WANT THE CUSTOM USER MODEL TO HAVE, (IF WE NEED THE CUSTOM USER MODEL AT ALL???)
#     email = models.EmailField(unique=True)

# WOULD THE FOODIE AND OWNER MODELS NEED TO INHERIT FROM THIS CUSTOM USER MODEL???

# class Foodie(User):
class Foodie(models.Model):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200, unique=True)
    google_calendar = models.URLField(unique=True, blank=True, null=True)


# class Owner(User):
class Owner(models.Model):
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200, unique=True)
    google_calendar = models.URLField(unique=True, blank=True, null=True)


class EateryVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(
        "Owner", related_name="eateries", on_delete=models.CASCADE
    )
