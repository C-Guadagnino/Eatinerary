# APIs

Notes to staff:
- The Cuisine Coders team is aware the format of this file is not as requested. Will ensure the format is as requested by next due date.

## Create home page
* **Method**: `GET`
* **Path**: /

## Create login
* **Method**: `POST`       
* **Path**: /login/foodie             
* **Path**: /login/owner

## Login redirect after signup
* **Method**: `POST`   
* **Path**: / login/redirect —> after user signs up, it redirects them to now log in (optional)

## Logout 
* **Method**: `GET`           
* **Path**: /logout

## Signup 
* **Method**: `POST`        
* **Path**: /signup/foodie         
* **Path**: /signup/owner


## Foodie Endpoints

## Gets a list of restaurants the foodie has skewered
* **Method**: `GET`          
* **Path**: /mySkewered

Output:
```json
{
	"skewered": [
		{
			"id": int,
			"created_datetime": {datetime object},
			"updated_datetime": {datetime object},
			"restaurant": {restaurant object} (nested object),
			"foodie": {foodie object},
			"has_visited": bool, default = false,
			"is_active": bool, default = true
		},
		{
			restaurant 2 info, etc.
		}
	]
}
```

## Details for specific restaurant that user skewered
* **Method**: `GET`          
* **Path**: /mySkewered/spotID/   

Output:
```json 
		{
			"id": int,
			"created_datetime": {datetime object},
			"updated_datetime": {datetime object},
			"restaurant": {restaurant object} (nested object),
			"foodie": {foodie object},
			"has_visited": bool, default = false,
			"is_active": bool, default = true
		}
```

## Adds restaurant to Foodie's list
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
	"has_visited": bool, default = false,
	"is_active": bool, default = true
}
```

## Deletes restaurant from foodie's list
* **Method**: `DELETE`    
* **Path**: /mySkewer/spotID/

Input:
```json 
{
	"id": int (required),
	"is_active": bool, false
}
```

Output:
```json
{
	"message": "Restaurant has been unskewered"
}
```

## Update details of skewered restaurant, adds notes, etc. 
* **Method**: `PUT`   
* **Path**: /mySkewer/spotID/         
"has_visited" field gets updated from false to true when the Foodie indicates they have visited the restaurant

Input:
```json 
{
	"id": int (required),
	"has_visited": bool, true 
}
```

Output:
```json
{
	"id": int,
	"created_datetime": {datetime object},
	"updated_datetime": {datetime object},
	"restaurant": {restaurant object},
	"foodie": {foodie object},
	"has_visited": bool, default = false,
	"is_active": bool, default = true
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
			"categories": {categories object},
			"hours": ???
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
			"categories": {categories object},
			"hours": ???
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
			"categories": {categories object},
			"hours": ???
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
	"foodie_location": coordinates(whatever Google Maps API returns), 
	"restaurant_id": int
}
```
Output:
```json
{
	"ETA": {time duration object}
}
```

## Get directions from current location to restaurant destination
* **Method**: `GET`    
* **Path**: /navigation

Input:
```json
{
	"foodie_location": coordinates(whatever Google Maps API returns), 
	"restaurant_id": int
}

Output:
```json
{
	"directions": Google Maps link
}
```



## Google Calendar

<!-- ## Owner gets a list of calendar dates
* **Method**: `GET`    
* **Path**: calendar/dates -->

## Owner creates a promotion for restaurant
* **Method**: `POST`   
* **Path**: /advertisements

Input:
```json
{
	"restaurant_id": int,
	"startdatetime": datetime,
	"enddatetime": enddatetime
}

Output:
```json
{
	"promotion_id": int,
	"message": "You successfully made a promotion!" 
}
```

Output:
```json
{
	"message": "Payment for promotion failed" 
}
```

## Owner lists promotions that they currently have going
* **Method**: `GET`   
* **Path**: /advertisements

Output:
```json
{
	"promotions": [
		{
			"restaurant_id": int,
			"startdatetime": datetime,
			"enddatetime": enddatetime
		},
		{
			promotion 2 info, etc..
		}
	]
}
```


## Owner updates a promotion
* **Method**: `PUT`   
* **Path**: /advertisements/promotion_id/

Input:
```json
{
		"promotion_id": int,
		"startdatetime": datetime,
		"enddatetime": enddatetime,
		"start_extension": datetime (stretch goal),
		"end_extension": datetime (stretch goal)
}

Output:
```json
{
		"promotion_id": int,
		"startdatetime": datetime,
		"enddatetime": enddatetime
}
```

## Owner gets details for a promotion
* **Method**: `GET`   
* **Path**: /advertisements/promotion_id/

Input:
```json
{
	"promotion_id": int,
}

Output:
```json
{
	"promotion_id": int,
	"startdatetime": datetime,
	"enddatetime": enddatetime
}
```

## Foodie creates special dates on calendar
* **Method**: `POST`
* **Path**: /specialDates

Input:
```json
{

}

Output:
```json
{
	
}
```

## Foodie lists special dates from calendar
* **Method**: `GET`
* **Path**: /specialDates

Input:
```json
{

}

Output:
```json
{
	
}
```

## Foodie gets a specific special date from calendar
* **Method**: `GET`
* **Path**: /specialDates/id/

Input:
```json
{

}

Output:
```json
{
	
}
```

## Foodie updates a special date from calendar
* **Method**: `PUT`
* **Path**: /specialDates/id/

Input:
```json
{

}

Output:
```json
{
	
}
```

## Foodie deletes a special date from calendar
* **Method**: `DELETE`
* **Path**: /specialDates/id/

Input:
```json
{

}

Output:
```json
{
	
}
```






