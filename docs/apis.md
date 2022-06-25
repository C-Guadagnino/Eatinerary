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

## Get a list of eateries the foodie has skewered
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
			"eatery": {eatery object} (nested object),
			"foodie": {foodie object} (nested object),
			"has_visited": bool,
			"is_active": bool
		},
		{
			eatery 2 info, etc.
		}
	]
}
```

## GET the details for a specific eatery that user skewered
* **Method**: `GET`
* **Path**: /mySkewered/spotID/

Output:
```json
		{
			"id": int,
			"created_datetime": string representing datetime object,
			"updated_datetime": string representing datetime object,
			"eatery": {eatery object} (nested object),
			"foodie": {foodie object} (nested object),
			"has_visited": bool,
			"is_active": bool
		}
```

## Add a eatery to Foodie's Skewered list
* **Method**: `POST`
* **Path**: /addToSkewer

Input:
```json
{
	"eatery": string,
	"foodie": string
}
```

Output:
```json
{
	"id": int,
	"created_datetime": {datetime object},
	"eatery": {eatery object},
	"foodie": {foodie object},
	"has_visited": bool (default = false),
	"is_active": bool (default = true)
}
```

## Remove eatery from foodie's Skewered list
* **Method**: `DELETE`
* **Path**: /mySkewer/spotID/
* Will not delete the eatery instance from the list, but instead, will update the "is_active" field from true to false

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
	"message": "Eatery has been unskewered"
}
```

## Update details of a specific skewered eatery, (STRETCH GOAL: adds notes, etc.)
* **Method**: `PUT`
* **Path**: /mySkewer/spotID/
* "has_visited" field gets updated from false to true when the Foodie indicates they have visited the eatery through GHI

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
	"eatery": {eatery object} (nested object),
	"foodie": {foodie object} (nested object),
	"has_visited": bool (will have been updated to true),
	"is_active": bool,
}
```

## Eatery endpoints

## Get a list of eateries from DB
* **Method**: `GET and POST`
* **Path**: /eateries/


Output:
```json
{
	"eateries": [
		{
			"id": int,
			"eatery_name": string,
			"email": string,
			"phone": str,
			"location": {location object} (nested object),
			"picture_url": str,
			"website": url,
			"yelp_id": str,
			"href": url,
			"review_count": int,
			"average_rating": int,
			"price": str,
			"from_yelp": boolean,
			"tags": manytomany,
			"categories": {categories object} (nested object),
			"open_hours": {open_hours object} {days_of_the_week object} (nested object),
			"eatery_images": {open_hours object} (nested object),
			"latitude": float,
			"longitude": float
		},
		{
			eatery 2 info, etc.
		}
	]
}
```

## Get a list of eateries from Yelp API
* **Method**: `GET`
* **Path**: /eateries/yelp/<location>/<category>/


Output:
```json
{
	"eateries": {
		"businesses": [
			{
			"id": int,
			"alias": str,
			"name": str,
			"image_url": url,
			"is_closed": boolean,
			"url": url,
			"review_count": int,
			"categories": [
				{
					"alias": str,
					"title": str
				}
			],
			"rating": int,
			"coordinates": {
				"latitude": float,
				"longitude": float
			},
			"transactions": [
				str
			],
			"price": str,
			"location": {
				"address1": str,
				"address2": str,
				"address3": str,
				"city": str,
				"zip_code": int,
				"country": str,
				"state": str
			},
			"phone": str,
			"display_phone": str,
			"distance": float
			},
	}
}
```

## Get details of a specific eatery
* **Method**: `GET`
* **Path**: /eateries/id

Output:
```json
		{
			"id": int,
			"eatery_name": string,
			"email": string,
			"phone": str,
			"location": {location object} (nested object),
			"picture_url": str,
			"website": url,
			"yelp_id": str,
			"href": url,
			"review_count": int,
			"average_rating": int,
			"price": str,
			"from_yelp": boolean,
			"tags": manytomany,
			"categories": {categories object} (nested object),
			"open_hours": {open_hours object} {days_of_the_week object} (nested object),
			"eatery_images": {open_hours object} (nested object),
			"latitude": float,
			"longitude": float
		}
```

## Get a list of eateries depending on the search_query
* **Method**: `GET`
* **Path**: /eateries/city/filter/<city>/
* **Example path**: /eateries/city/filter/denver/ —> lists all eateries in denver

Output:
```json
{
	"eateries": [
		{
			"id": int,
			"eatery_name": string,
			"email": string,
			"phone": str,
			"location": {location object} (nested object),
			"picture_url": str,
			"website": url,
			"yelp_id": str,
			"href": url,
			"review_count": int,
			"average_rating": int,
			"price": str,
			"from_yelp": boolean,
			"tags": manytomany,
			"categories": {categories object} (nested object),
			"open_hours": {open_hours object} {days_of_the_week object} (nested object),
			"eatery_images": {open_hours object} (nested object),
			"latitude": float,
			"longitude": float
		},
		{
			eatery 2 info, etc.
		}
	]
}
```
## Get a list of eatery locations
* **Method**: `GET and POST`
* **Path**: /eateries/locations/

Output:
```json
{"locations": [
		{
			"href": url,
			"id": int,
			"address1": str,
			"address2": str,
			"address3": str,
			"city": str,
			"state": str,
			"zip_code": int,
			"country": str
		},
		{
			eatery 2 info, etc.
		}
	]
}
```

## Get one eatery location
* **Method**: `GET`
* **Path**: /eateries/locations/<id>/

Output:
```json
{"locations": 
		{
			"href": url,
			"id": int,
			"address1": str,
			"address2": str,
			"address3": str,
			"city": str,
			"state": str,
			"zip_code": int,
			"country": str
		},
	
}
```
## Get a list of categories
* **Method**: `GET and POST`
* **Path**: /eateries/categories/

Output:
```json
{"categories": [
		{
			"href": url,
			"id": int,
			"alias": str,
			"title": str
		},
		{
			eatery 2 info, etc.
		}
	]
	
}
```

## Get one category
* **Method**: `GET`
* **Path**: /eateries/category/<id>/

Output:
```json
{"category": 
		{
			"href": url,
			"id": int,
			"alias": str,
			"title": str
		},
	
}
```

## Get a list of tags
* **Method**: `GET and POST`
* **Path**: /eateries/tags/

Output:
```json
{"tags": [
		{
			"tag_name": str,
		},
		{
			eatery 2 info, etc.
		}
	]
}
```

## Get one tags
* **Method**: `GET`
* **Path**: /eateries/tags/<tag_name>

Output:
```json
{"tags": 
		{
			"tag_name": str,
		},
	
}
```

## Get a list of open_hours
* **Method**: `GET and POST`
* **Path**: /eateries/open_hours/

Output:
```json
{"open_hours": [
		{
			"eatery": url,
			"weekday": int,
			"start_time": time,
			"end_time": time
		},
		{
			eatery 2 info, etc.
		}
]
}
```

## Get one open_hours
* **Method**: `GET`
* **Path**: /eateries/open_hours/<id>

Output:
```json
{"open_hours": 
		{
			"eatery": url,
			"weekday": int,
			"start_time": time,
			"end_time": time
		},

}
```
## Get one eatery_image
* **Method**: `GET`
* **Path**: /eateries/eatery_images/<id>

Output:
```json
{"eatery_image": 
		{
			"image_url": url,
			"eatery": {eatery object} (nested object)
		},

}
```

## Foodies microservice

## List all Foodies
* **Method**: `GET`
* **Path**: /foodies
* returns a list of all foodies, including the eateries they skewered and special dates 

Output:
```json
{
    "foodies":
		{
			"username": string representing the username,
			"first_name": string representing the foodies firstname,
			"email": string representing the foodies email,
			"phone": int representing the foodies phone number,
			"skewered_eateries": [
				{
					"id": int,
					"created_DateTime": string representing datetime object ,
					"updated_DateTime": string representing datetime object,
					"has_visited": bool,
					"is_active": bool,
					"notes": string representing the foodies notes for a skewered eatery,
					"eatery": {
						"eatery_name": string representing eatery name,
						"eatery_import_href": string identify the eatery object,
						"eatery_price": string representing the cost of the eatery,
						"eatery_average_rating": int,
						"eatery_location_city": string representing the city of the eatery,
						"eatery_location_state": string representing the state of the eatery,
						"eatery_latitude": string, with the eatery latitude ,
						"eatery_longitude": string with the eatery longitude,
					},
					"foodie": {
						"foodie_username": string with the foodie's username,
						"foodie_firstname": string with the foodie's firstname,
						"foodie_lastname": string with the foodie's last name
					}
				},
			],
			"special_dates": [
				{
					"id": int,
					"special_date": string representing the date of the occasion,
					"occasion": string representing the reason for the occasion,
					"has_passed": bool,
					"repeats": bool,
					"frequency": string representing if the special date is yearly
				}
			]
		}
	]
```

## Create a Foodie
* **Method**: `POST`
* **Path**: /foodies
* create a foodie 

Input:
```json
        {
            "username": string representing the username of the foodie,
            "first_name": string representing the name of the foodie,
            "email": string representing the email of the foodie,
            "phone": string representing the phone number of the foodie
        }
```

Output:
```json 
{
	"username": string representing the username of the foodie,
    "first_name": string representing the name of the foodie,
    "email": string representing the email of the foodie,
    "phone": string representing the phone number of the foodie,
	"skewered_eateries": [list of skewered eatery objects]
}
```

## Get details of a Foodie
* **Method**: `GET`
* **Path**: /foodies/user/<str:username>/
* Get the details of a specific foodie based on their username

Output:
```json
    {
    "href": string,
	"username": string representing the username of the foodie,
    "first_name": string representing the name of the foodie,
    "email": string representing the email of the foodie,
    "phone": string representing the phone number of the foodie,
	"skewered_eateries": [list of skewered eatery objects]
}
```
## Get all Eatery VOs
* **Method**: `GET`
* **Path**: /foodies/eateries/
* Get a list of all the eatery value objects 

Output:
```json
    {
	"eateries": [
		{
			"import_href": string,
			"eatery_name": string,
			"email": string,
			"phone":string,
			"website": string,
			"yelp_id": string,
			"review_count": int,
			"average_rating": int,
			"price": string,
			"from_yelp": bool,
			"location_address1": string,
			"location_address2":string,
			"location_address3": string,
			"location_city": string,
			"location_state":string,
			"location_zip": string,
			"location_country": string,
			"latitude": string,
			"longitude": string,
			"tagsvo": [list of tag objects],
			"categoriesvo": [
				{
					"import_href": string,
					"alias": string,
					"title": string
				},
			],
			"eateryimagesvo": [
				{
					"import_href": string,
					"image_url": string
				}
			],
			"allopenhoursvo": [
				{
					"import_href": string,
					"weekday": string,
					"start_time": string,
					"end_time": string
				},
			],
			"reviews": [list of review objects],
			"skewered_eateries": [list of skewered eateries objects]
		}
```
## Get details of an Eatery VO
* **Method**: `GET`
* **Path**: foodies/eateries/<int:eatery_entity_id>/
* Get the details of an eatery value object

```json
    {
	"eateries": [
		{
			"import_href": string,
			"eatery_name": string,
			"email": string,
			"phone":string,
			"website": string,
			"yelp_id": string,
			"review_count": int,
			"average_rating": int,
			"price": string,
			"from_yelp": bool,
			"location_address1": string,
			"location_address2":string,
			"location_address3": string,
			"location_city": string,
			"location_state":string,
			"location_zip": string,
			"location_country": string,
			"latitude": string,
			"longitude": string,
			"tagsvo": [list of tag objects],
			"categoriesvo": [
				{
					"import_href": string,
					"alias": string,
					"title": string
				},
			],
			"eateryimagesvo": [
				{
					"import_href": string,
					"image_url": string
				}
			],
			"allopenhoursvo": [
				{
					"import_href": string,
					"weekday": string,
					"start_time": string,
					"end_time": string
				},
			],
			"reviews": [list of review objects],
			"skewered_eateries": [list of skewered eateries objects]
		}
```
## Get all Categories VO
* **Method**: `GET`
* **Path**: foodies/eateries/categories/
* Get all of the categories associated with an eatery

Output:
```json
    {
	"eatery_categories": [
		{
			"import_href": string,
			"alias": string,
			"title": string,
		},
```

## Get a specific Category VO
* **Method**: `GET`
* **Path**: foodies/eateries/categories/<str:alias/>
* Get a specific category associated with an eatery

Output:
```json
    {
	"import_href": string,
	"alias": string,
	"title": string,
	"eatery": {
		"eatery_name": string,
		"eatery_import_href": string,
	}
}
```

## Get all Eatery Tags VO
* **Method**: `GET`
* **Path**: foodies/eateries/tags/
* Get all eatery tags associated with an eatery

Output:
```json
    {
    "tags": [
        {
        "import_href": string,
        "tag_name": string,
        "eatery": {
            "eatery_name": string,
            "eatery_import_href": string
        }
    ]
}
```
## Get a specific Eatery Tags VO
* **Method**: `GET`
* **Path**: foodies/eateries/tags/<str:tag_name>/
* Get a specific eatery tag associated with an eatery

Output:
```json
    {
	"import_href": string,
	"tag_name": string,
	"eatery": {
		"eatery_name": string,
		"eatery_import_href": string
	}
}
```

## Get all OpenHoursVO
* **Method**: `GET`
* **Path**: foodies/eateries/openhours/
* Get all of the open hours for eateryVOs

Output:
```json
{
	"eatery_open_hours_all": [
		{
			"import_href": string,
			"weekday":string,
			"start_time": string,
			"end_time": string
		},
    ]
}
```
## Get a specific OpenHoursVO
* **Method**: `GET`
* **Path**: foodies/eateries/openhours/<int:eatery_openhours_entity_id>/
* Get one specific set of open hours for an eateryVO


Output:
```json
    	{
			"import_href": string,
			"weekday": string,
			"start_time": string,
			"end_time": string
		},
```

## Get all EateryImagesVO
* **Method**: `GET`
* **Path**: foodies/eateries/images/
* Get all of the eatery images for eateryVOs

Output:
```json
{
	"eatery_images": [
		{
			"import_href": string,
			"image_url": string
		},
    ]
}
```

## Get a Specific Foodie User
* **Method**: `GET`
* **Path**: /api/users/id
Output
```json
{
    “id”: int,
    “username”: string,
    “email”: string,
}
```
## Create A Review Image
* **Method**: `POST`
* **Path**: /api/foodies/eateries/reviews/images/
Input
```json
{
    “image_url”: string,
    “review”: int
}
Output
```json
{
    “id”: int,
    “image_url”: string
}
```
## Get all Review Images
* **Method**: `GET`
* **Path**: /api/foodies/eateries/reviews/images/
Output
```json
{
    “review_images”: [
        {
            “id”: int,
            “image_url”: string
        }
    ]
}
```
## Get a specific Review Image
* **Method**: `GET`
* **Path**: /api/foodies/eateries/reviews/images/id/
Output
```json
“review_image”: {
    “id”: int,
    “image_url”: string
}
```
## Foodie deletes a Review Image
* **Method**: `DELETE`
* **Path**: /api/foodies/eateries/reviews/images/id/
Output
```json
{
    “deleted” : boolean
}
```
## Create A Review * **Method**: `POST`
* **Path**: /api/foodies/eateries/reviews/
Input
```json
{
    “title”: string,
    “rating”: int,
    “description”: string,
    “skewered_eatery”: int
}
Output
```json
{
    “id”: int,
    “title”: string,
    “rating”: int,
    “created_DateTime”: string,
    “description”: string,
    “review_images”: array,
    “skewered_eatery”: {
        “id”: int,
        “created_DateTime”: string,
        “updated_DateTime”: string,
        “has_visited”: boolean,
        “is_active”: boolean,
        “notes”: ,
        “eatery”: {
            {eatery_object}
        },
        “foodie”: {
            {foodie_object}
        }
    }
}
```
## Foodie deletes a Review * **Method**: `DELETE`
* **Path**: /api/foodies/eateries/reviews/id/
Output
```json
{
    “deleted” : boolean
}
```



#### FUTURE DEVELOPMENT:


## Google Maps endpoints

## Get ETA from current location to eatery destination
* **Method**: `GET`
* **Path**: /ETA

Input:
```json
{
	"foodie_location": coordinates (whatever Google Maps API requires as input),
	"eatery_id": int
}
```
Output:
```json
{
	"ETA": string representing time duration (may be slightly different depending on what the Google Maps API returns)
}
```

## Get directions from current location to eatery destination
* **Method**: `GET`
* **Path**: /navigation

Input:
```json
{
	"foodie_location": coordinates (whatever Google Maps API requires as input),
	"eatery_id": int
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

## Owner creates an ad_slot for eatery
* **Method**: `POST`
* **Path**: /advertisements

Input:
```json
{
	"eatery_id": int,
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
			"eatery_id": int,
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






