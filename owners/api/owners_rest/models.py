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
    # JK!!!!!!!!!! we decided that our app will display eateries from yelp even BEFORE an owner claims them
    # Question: Can ForeignKeys take null=True, blank=True? Test this out later.

    # comment out once OwnerVO model is ready
    # owner = models.ForeignKey(
    #     "OwnerVO",
    #     related_name="eateries",
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    # )

    eatery_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone = models.CharField(max_length=200)
    # ??? What should the location attribute be?
    # Just a TextField? OR
    # If a OneToOne field, how to connect to EateryLocation from Eateries MS? Poll from EateryLocation and populate EateryLocationVO model in this MS?
    # location = models.OneToOneField(
    #     "EateryLocation", related_name="eatery", on_delete=models.CASCADE
    # )
    website = models.URLField(max_length=200, unique=True)
    # we might not need this, but keep it in here for convenience for now since yelp API will provide it
    yelp_id = models.CharField(max_length=200, unique=True)
    # what was href for??? Need to refresh memory
    # href = models.URLField(max_length=200, unique=True)
    review_count = models.PositiveSmallIntegerField(default=0)
    average_rating = models.FloatField()
    # "$$"
    price = models.CharField(max_length=4)
    # should this go in the EateryVO model or bring over Tag from Eateries MS and populate TagVO???
    # tag = models.ManyToManyField("TagVO")

    # ??? What should the categories attribute be?
    # Just a CharField? OR
    # If a ManyToMany field, how to connect to EateryCategory from Eateries MS? Poll from EateryCategory and populate EateryCategoryVO model in this MS?
    # categories = models.ManyToManyField("EateryCategory", related_name="categories")


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
