# APIs


## Create home page
* **Method**: `GET`
* **Path**: /
* returns home page of the app. Maybe this is not an API endpoint, but just a web/GHI endpoint?

## Login
* **Method**: `POST`
* **Path**: /login/foodie
* **Path**: /login/owner
* Logs in the foodie in the /login/foodie endpoint, and logs in the owner in the /login/owner endpoint. Maybe these are not API endpoints, but just web/GHI endpoints?

## Logout
* **Method**: `GET`
* **Path**: /logout
* Logs the user out of their account. Maybe this is not an API endpoint, but just a web/GHI endpoint?

## Signup
* **Method**: `POST`
* **Path**: /signup/foodie
* **Path**: /signup/owner
* Signs up foodie/owner by creating an instance of foodie/owner


## Foodie Endpoints

## Get a list of restaurants the foodie has skewered
* **Method**: `GET`
* **Path**: /mySkewered

Output:
```json
{
	"skewered": [
		{
			"id": int,
			"created_datetime": string representing datetime object,
			"updated_datetime": string representing datetime object,
			"restaurant": {restaurant object} (nested object),
			"foodie": {foodie object} (nested object),
			"has_visited": bool,
			"is_active": bool
		},
		{
			restaurant 2 info, etc.
		}
	]
}
```

## GET the details for a specific restaurant that user skewered
* **Method**: `GET`
* **Path**: /mySkewered/spotID/

Output:
```json
		{
			"id": int,
			"created_datetime": string representing datetime object,
			"updated_datetime": string representing datetime object,
			"restaurant": {restaurant object} (nested object),
			"foodie": {foodie object} (nested object),
			"has_visited": bool,
			"is_active": bool
		}
```

## Add a restaurant to Foodie's Skewered list
* **Method**: `POST`
* **Path**: /addToSkewer

Input:
```json
{
	"restaurant": string,
	"foodie": string
}
```

Output:
```json
{
	"id": int,
	"created_datetime": {datetime object},
	"restaurant": {restaurant object},
	"foodie": {foodie object},
	"has_visited": bool (default = false),
	"is_active": bool (default = true)
}
```

## Remove restaurant from foodie's Skewered list
* **Method**: `DELETE`
* **Path**: /mySkewer/spotID/
* Will not delete the restaurant instance from the list, but instead, will update the "is_active" field from true to false

Input:
```json
{
	"id": int (required),
	"is_active": bool (will update from true to false)
}
```

Output:
```json
{
	"message": "Restaurant has been unskewered"
}
```

## Update details of a specific skewered restaurant, (STRETCH GOAL: adds notes, etc.)
* **Method**: `PUT`
* **Path**: /mySkewer/spotID/
* "has_visited" field gets updated from false to true when the Foodie indicates they have visited the restaurant through GHI

Input:
```json
{
	"id": int (required),
	"has_visited": bool (true)
}
```

Output:
```json
{
	"id": int,
	"created_datetime": string representing datetime object,
	"updated_datetime": string representing datetime object,
	"restaurant": {restaurant object} (nested object),
	"foodie": {foodie object} (nested object),
	"has_visited": bool (will have been updated to true),
	"is_active": bool,
}
```

## Restaurant endpoints

## Get a list of restaurants from Yelp API
* **Method**: `GET`
* **Path**: /restaurants/


Output:
```json
{
	"restaurants": [
		{
			"owner": string,
			"restaurant_name": string,
			"email": string,
			"phone": str,
			"location": ???,
			"google_calendar": url,
			"picture_url": str,
			"website": url,
			"yelp_id": str,
			"href": url,
			"review_count": int,
			"average_rating": int,
			"price": str,
			"categories": {categories object} (nested object),
			"hours": ??? (ideally nested object with each day's hours)
		},
		{
			restaurant 2 info, etc.
		}
	]
}
```

## Get details of a specific restaurant
* **Method**: `GET`
* **Path**: /restaurants/id

Output:
```json
		{
			"owner": string,
			"restaurant_name": string,
			"email": string,
			"phone": str,
			"location": ???,
			"google_calendar": url,
			"picture_url": str,
			"website": url,
			"yelp_id": str,
			"href": url,
			"review_count": int,
			"average_rating": int,
			"price": str,
			"categories": {categories object} (nested object),
			"hours": ??? (ideally nested object with each day's hours)
		}
```

## Get a list of restaurants depending on the search_query
* **Method**: `GET`
* **Path**: /restaurants/search_query
* **Example path**: /restaurants/bbq/ —> lists all restaurants that have bbq

Output:
```json
{
	"restaurants": [
		{
			"owner": string,
			"restaurant_name": string,
			"email": string,
			"phone": str,
			"location": ???,
			"google_calendar": url,
			"picture_url": str,
			"website": url,
			"yelp_id": str,
			"href": url,
			"review_count": int,
			"average_rating": int,
			"price": str,
			"categories": {categories object} (nested object),
			"hours": ??? (ideally nested object with each day's hours)
		},
		{
			restaurant 2 info, etc.
		}
	]
}
```

## Google Maps endpoints

## Get ETA from current location to restaurant destination
* **Method**: `GET`
* **Path**: /ETA

Input:
```json
{
	"foodie_location": coordinates (whatever Google Maps API requires as input),
	"restaurant_id": int
}
```
Output:
```json
{
	"ETA": string representing time duration (may be slightly different depending on what the Google Maps API returns)
}
```

## Get directions from current location to restaurant destination
* **Method**: `GET`
* **Path**: /navigation

Input:
```json
{
	"foodie_location": coordinates (whatever Google Maps API requires as input),
	"restaurant_id": int
}

Output:
```json
{
	"directions": Google Maps link (may be slightly different depending on what the Google Maps API returns)
}
```



## Google Calendar

<!-- ## Owner gets a list of calendar dates
* **Method**: `GET`
* **Path**: calendar/dates -->

## Owner creates an ad_slot for restaurant
* **Method**: `POST`
* **Path**: /advertisements

Input:
```json
{
	"restaurant_id": int,
	"startdatetime": datetime obj/str(?) representing start date and time,
	"enddatetime": datetime obj/str(?) representing end date and time
}

Output:
```json
{
	"ad_slot_id": int,
	"message": "You have successfully reserved an advertisement slot!"
}
```

Output:
```json
{
	"message": "Payment for ad_slot failed"
}
```

## Owner lists ad slots that they currently have going
* **Method**: `GET`
* **Path**: /advertisements

Output:
```json
{
	"ad_slots": [
		{
			"restaurant_id": int,
			"startdatetime": string representing start date & time,
			"enddatetime": string representing end date & time
		},
		{
			ad_slot 2 info, etc..
		}
	]
}
```


## Owner updates an ad_slot (STRETCH GOAL)
* **Method**: `PUT`
* **Path**: /advertisements/ad_slot_id/

Input:
```json
{
		"ad_slot_id": int,
		"startdatetime": start datetime,
		"enddatetime": end datetime,
		"start_extension": time duration (to extend startdatetime),
		"end_extension": time duration (to extend enddatetime)
}

Output:
```json
{
		"ad_slot_id": int,
		"startdatetime": datetime obj/str(?),
		"enddatetime": datetime obj/str(?)
}
```

## Owner gets details for an ad_slot
* **Method**: `GET`
* **Path**: /advertisements/ad_slot_id/

Input:
```json
{
	"ad_slot_id": int,
}

Output:
```json
{
	"ad_slot_id": int,
	"startdatetime": datetime obj/str(?),
	"enddatetime": datetime obj/str(?)
}
```

## Foodie creates special dates on calendar
* **Method**: `POST`
* **Path**: /specialDates

Input (TBD -- will depend on what Google Calendar API takes as input):
```json
{

}

Output (TBD -- will depend on what Google Calendar API returns as output):
```json
{

}
```

## Foodie lists special dates from calendar
* **Method**: `GET`
* **Path**: /specialDates

Input (TBD -- will depend on what the Google Calendar API takes as input):
```json
{

}

Output (TBD -- will depend on what the Google Calendar API returns as output):
```json
{

}
```

## Foodie gets a specific special date from calendar
* **Method**: `GET`
* **Path**: /specialDates/id/

Input (TBD -- will depend on what the Google Calendar API takes as input):
```json
{

}

Output (TBD -- will depend on what the Google Calendar API returns as output):
```json
{

}
```

## Foodie updates a special date from calendar
* **Method**: `PUT`
* **Path**: /specialDates/id/

Input (TBD -- will depend on what the Google Calendar API takes as input):
```json
{

}

Output (TBD -- will depend on what the Google Calendar API returns as output):
```json
{

}
```

## Foodie deletes a special date from calendar
* **Method**: `DELETE`
* **Path**: /specialDates/id/

Input (TBD -- will depend on what the Google Calendar API takes as input):
```json
{

}

Output (TBD -- will depend on what the Google Calendar API returns as output):
```json
{

}
```






