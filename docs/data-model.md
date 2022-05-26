# Data models

## Foodie
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| username        | str     | yes    | no       |
| first_name      | str     | no     | no       |
| last_name       | str     | no     | no       |
| email           | str     | yes    | no       |
| phone           | int     | yes    | no       |
| usertype        | str     | no     | no       |
| google_calendar | url?    | yes    | no       |


## Restaurant_owner
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| username        | str     | yes    | no       |
| first_name      | str     | no     | no       |
| last_name       | str     | no     | no       |
| email           | str     | yes    | no       |
| phone           | int     | yes    | no       |
| usertype        | str     | no     | no       |
| google_calendar | url?    | yes    | no       |
| restaurant      | For.Key | yes    | no       |

## Restaurant
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| owner           | For.Key | no     | no       |
| restaurant_name | str     | no     | no       |
| email           | str     | yes    | yes      |
| phone           | int     | yes    | yes      |
| location        | For.Key | no     | no       |
| google_calendar | url?    | yes    | no       |
| availability    | For.Key | no     | no       |
| picture_url     | str     | no     | no       |
| website         | url     | no     | yes      |
| yelp_id         | str     | no     | no       |
| href            | url     | no     | yes      |
| review_count    | int     | yes    | yes      |
| average_rating  | int     | yes    | yes      |
| price           | str     | yes    | yes      |
| categories      |ManyToMany? not sure about how to model restaurant categories. ManyToMany Field, since 1 restaurant can have many restaurant categories, and 1 category can have many restaurants?| yes  | yes      |
| mon_open_hours  | For.Key | yes    | yes      |
| tue_open_hours  | For.Key | yes    | yes      |
| wed_open_hours  | For.Key | yes    | yes      |
| thu_open_hours  | For.Key | yes    | yes      |
| fri_open_hours  | For.Key | yes    | yes      |
| sat_open_hours  | For.Key | yes    | yes      |
| sun_open_hours  | For.Key | yes    | yes      |


## Restaurant_categories???
https://www.yelp.com/developers/documentation/v3/get_started

| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| alias           | str     | no     | no       |
| title           | str     | no     | no       |

## Restaurant_location
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| address1        | str     | no     | no       |
| address2        | str     | no     | yes      |
| address3        | str     | no     | yes      |
| city            | str     | no     | no       |
| state           | str     | no     | no       |
| zip             | int     | no     | no       |
| country         | str     | no     | no       |

## Restaurant_open_hours
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| start           | str?int?| no     | no       |
| end             | str?int?| no     | no       |
| day (mon-fri)   | int(0-7)| no     | no       |


## Skewered
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| restaurant      | For.Key | yes    | no       |
| foodie          | For.Key | yes    | yes      |
| created_DateTime| date    | no     | no       |
| has_visited     | bool    | no     | no       |

## Reservation
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| foodie          | For.Key | no     | no       |
| restaurant      | For.Key | no     | no       |
| datetime        | DateTime| no     | no       |
| num_guests      | int     | no     | no       |
| special_requests| str     | no     | yes      |

## Review
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| title           | str     | no     | no       |
| rating          | int     | no     | no       |
| created_DateTime| date    | no     | no       |
| description     | str     | no     | no       |
| picture1        |media/url? should we require picture_url, or allow Foodie to upload image directly? (Need to look into this)| no    | yes      |
| picture2        |media/url?| no    | yes      |
| picture3        |media/url?| no    | yes      |
| picture4        |media/url?| no    | yes      |
| picture5        |media/url?| no    | yes      |
| picture6        |media/url?| no    | yes      |
| picture7        |media/url?| no    | yes      |
| picture8        |media/url?| no    | yes      |
| picture9        |media/url?| no    | yes      |
| picture10       |media/url?| no    | yes      |
| skewered        | OneToOne| no     | no       |
OR
| foodie          | For.Key | no     | no       |
| restaurant      | For.Key | no     | no       |

(skewered OR foodie+restaurant???)


## Ad_slot (for each continuous time slot)
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| restaurant      | For.Key | no     | no       |
| startdatetime   | DateTime| no     | no       |
| enddatetime     | DateTime| no     | no       |


## Payment
- We believe we should not need a payment model to even temporarily store payment information
- This will depend on what Stripe API requires - ideally we don't want to handle payment info directly for security/liability reasons (and let alone storing it)

