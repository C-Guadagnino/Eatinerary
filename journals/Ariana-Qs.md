# Ariana's questions

1)
* Q: Can we change our App name to "Eatinerary"? If so, would we be able to leave the repo/project name intact as "Restaurant-repo", or do we need to make all those changes? Best practice?
* A: Per Curtis, not hard at all! Just need a few easy steps on Gitlab. He recommended we do it once we finish the project.

2)
* Q: Do we need API endpoints to support the signup/login pages? We have used the Django built-in signup/login functionalities in past projects, and these did not need API endpoints (since Django handled them directly).
* A:

3)
* Q: In past projects (Conference-GO/Fearless Frontend) when an attendee created an account, then we used the Django's built-in User model to create a User model instance and the AccountVO model got data from the that (Django's built-in) user model. Will we still be using Django's user model for this Restaurant-repo project? what would that look like?
* A:

4)
* Q: For ubiquitous language: should we decide on "promotion slot" or "ad slot" or something else? Need to decide on something and make it consistent throughout models and APIs
* A: Cuisine Coders decided on "Ad slot"

5)
* Q: How should "location" be defined -- for example, for when foodies search for eateries in a location, or owners book an ad_slot for their eatery?
* A: Per Curtis, it can be a city name for when foodies search for eateries for a location ("philadelphia"), and it can be a zip code for ad_slots! Just start with one, and we can always update later.