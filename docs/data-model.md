# Data models

## Foodie
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| username        | str     | yes    | no       |
| first_name      | str     | no     | no       |
| last_name       | str     | no     | no       |
| email           | str     | yes    | no       |
| phone           | int     | yes    | no       |
| google_calendar | url?    | yes    | no       |


## Restaurant_owner
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| username        | str     | yes    | no       |
| first_name      | str     | no     | no       |
| last_name       | str     | no     | no       |
| email           | str     | yes    | no       |
| phone           | int     | yes    | no       |
| google_calendar | url?    | yes    | no       |
| restaurant      | For.Key | yes    | no       |

## Restaurant
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| owner           | For.Key | no     | no       |
| restaurant_name | str     | no     | no       |
| email           | str     | yes    | yes      |
| phone           | str     | yes    | yes      |
| location        | For.Key | no     | no       |
| google_calendar | url?    | yes    | no       |
| image     | str     | no     | no       |
| website         | url     | no     | yes      |
| yelp_id         | str     | no     | no       |
| href            | url     | no     | yes      |
| review_count    | int     | yes    | yes      |
| average_rating  | int     | yes    | yes      |
| price           | str     | yes    | yes      |
| categories      |ManyToMany? not sure about how to model restaurant categories. ManyToMany Field, since 1 restaurant can have many restaurant categories, and 1 category can have many restaurants?| yes  | yes      |


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
| zip             | str     | no     | no       |
| country         | str     | no     | no       |

## Restaurant_open_hours (one-to-many relationship between Restaurant and Restaurant_open_hours)
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| id              | int     | yes    | no       |
| start           | str?int?| no     | no       |
| end             | str?int?| no     | no       |
| day (mon-fri)   | int(0-7)| no     | no       |


## Skewered
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| restaurant      | For.Key | yes    | no       |
| foodie          | For.Key | yes    | yes      |
| created_DateTime| date    | no     | no       |
| updated_DateTime| date    | no     | no       |
| has_visited     | bool    | no     | no       |
| is_active       | bool    | no     | no       |
| tag             |Many2Many| no     | no       |
| notes           | str/ textfield   | no     | no       |

## Tag VO (many-to-many relationship between Tag and Skewered. #datenight #brunch, etc. Tags are created by foodie and are specific to that foodie only, so they can search for #datenight #brospot or whatever whey had marked a skewered restaurant as.
* Discuss with Cuisine Coders whether we want the tags to be related to Restaurants instead of Skewered restaurants, and for the tags to be visible by everyone instead of just by the foodie that created them. That way the whole RestaurantRepo community can benefit from the tags other people add to Restaurants, and can even search/filter by those tags.)
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| tag             | str     | yes    | no       |


## Review
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| title           | str     | no     | no       |
| rating          | int     | no     | no       |
| created_DateTime| date    | no     | no       |
| description     | str     | no     | no       |
| skewered        | OneToOne| no     | no       |
| image           | For.Key | no     | yes      |


## Image VO (one-to-many relationship between review and picture)
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| image_url       | media/url? should we require picture_url, or allow Foodie to upload image directly? (Need to look into this, and implications of user experience vs resources taken up for loading app when existing number of images in app increase dramatically)     | yes    | no       |


## Ad_slot (for each continuous time slot)
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| restaurant      | For.Key | no     | no       |
| startdatetime   | DateTime| no     | no       |
| enddatetime     | DateTime| no     | no       |


## Payment
- We believe we should not need a payment model to even temporarily store payment information
- This will depend on what Stripe API requires - ideally we don't want to handle payment info directly for security/liability reasons (and let alone storing it)

