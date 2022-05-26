#APIs

Notes to staff:
- The Cuisine Coders team is aware the format of this file is not as requested. Will ensure the format is as requested by next due date.

## Create home page
* Method: GET          / for home page

## Create login/logout/signup
* Method: POST       /login/foodie             /login/owner
* Method: GET           /logout
* Method: POST        /signup/foodie         /signup/owner
* Method: POST (?)   / login/redirect —> after user signs up, it redirects them to now log in (optional)

## Foodie Interface
* Method: GET          /mySkewered                 (lists restaurants that user skewered)
* Method: GET          /mySkewered/spotID/    (details for specific restaurant that user skewered)
* Method: POST        /addToSkewer               (adds restaurant to Foodie's list)
* Method: DELETE    /mySkewer/spotID/        (Foodie deletes restaurant from their list)
* Method: UPDATE   /mySkewer/spotID/         ("has_visited" field gets updated from false to true when the Foodie indicates they have visited the restaurant; or Foodie updates details of the skewered restaurant, adds notes in there like, “GF or BF wants to eat here”, “Mom’s fav spot”, etc.

## Yelp endpoints
* Method: GET     /restaurants/search_query
       				 /restaurants/bbq/ —> lists all restaurants that have bbq

* Method: GET   /restaurants/search_query/id   (show details for that restaurant)
				/restaurants/bbq/23/

## Google Maps endpoints
* Method: GET    /trafficInfo
* Method: GET    /navigation

## Open Table endpoints
* Method: GET   api/restaurants
* Method: GET   api/restaurants/:id

## Google Calendar
* Method: GET    api/dates
* Method: POST   api/reservation, api/advertisements, api/specialDates

