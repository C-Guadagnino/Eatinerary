# App name: Restaurant Repo

## Design

* [API design](docs/apis.md)
* [Data model](docs/data-model.md)
* [GHI](docs/ghi.md)
* [Integrations](docs/integrations.md)

## Team name: The Cuisine Coders

## List of team members:
* Ariana Kim
* Cameron Guadagnino
* Brandon Dix
* David Quinlan


## Summary:
* Detailed collection of eateries that have garnered interest
* Tagline: "Fastest way to access all eateries you may have missed"

## Intended Market:
The people that we expect to use this are:
* "Diners"/"Foodies" that range from 16yrs+, who are interested in being reminded in eateries they’re interested in.
* Eatery owners who are interested in gaining exposure and advertising their eatery business advertising.


## Ubiquitous language (work in progress):
* "Diner"/"Foodie": Individual user/consumer of the app that is interested in being reminded in eateries they're interested in.
* Eatery owner: Owner of a eatery that has an account/profile - manages a eatery or many eateries
* Eatery: a single eatery location/business
* "Skewer": The action of a Diner/Foodie saving/pinning/favorite-ing a eatery to their list of saved/"skewered" eateries


## Functionality:
* Create account/profile
    * "Diners"/"Foodies" can create a diner/foodie account/profile
    * Eatery owners can create a eatery owner account/profile
* Login/Logout
    * Users ("diners"/"foodies" and eatery owners) can login/logout of account/profile
* Search feature for the eateries
    * create filter system
        * Filter criteria: eatery name, cuisine, reservation date and time, location
* Link Yelp API
    * list of eateries, reviews, hours of operation, photos
    * Get and post(?) ratings
* Link Google Maps or other mapping API
    * Embed map into app
    * “Busy” right now
    * App should show a view of a map where it shows "pins" of all the skewered locations
    * Traffic patterns & ETA from diner/foodie's current location to skewered location/s
* Email functionality
    * Send email notification to diner/food when a eatery is skewered
        * Email to include links to make reservations (online reservation site, phone number)
    * (STRETCH GOAL) Send email notification to eatery owner when an ad_slot is booked/reserved.
* Link Calendar (Google calendar API?)
    * There will be a calendar per city/zip (TBD by CuisineCoders) that keeps track of advertisement slots.
        * Eatery owners can pay for advertisement slots to have their eatery show up higher on searches during specific times. For example, a eatery owner can pay $x (TBD on how the price will be set) for the 6-7pm slot on specific dates, so their eatery will show up toward the top of the page when a diner/foodie searches for eateries in that city/zip (TBD by CuisineCoders) during 6-7pm on the specific dates the eatery owner paid for.
    * Each foodie can choose to have their own calendar to save special days (birthdays, anniversaries, holidays, etc). The app will suggest eateries from the list of eateries that the diner/foodie has “skewered” (saved/pinned/favorited).
* Chat feature via websockets
    * Diner/foodie can contact hostess of eatery and let them know they’re running late, on their way, etc. for reservation
* Payment system (Stripe API?)
    * Integrate some sort of payment system on the app so eatery owner can independently click, choose and pay for ad slots (refer to second bullet point in "Link Calendar" section above). This is a way for the eatery owners to increase exposure and traffic flow to eatery
* Light/Dark mode
* Mobile responsive
