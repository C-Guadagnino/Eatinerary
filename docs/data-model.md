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
| restaurant_name | str     | no     | no       |
| email           | str     | yes    | yes      |
| phone           | int     | yes    | yes      |
| location        | For.Key | no     | no       |
| google_calendar | url?    | yes    | no       |
| availability    | For.Key | no     | no       |
| picture_url     | str     | no     | no       |
| website         | url     | no     | yes      |
| href            | url     | no     | yes      |
| review_count    | str     | yes    | yes      |

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
| picture1        |media/url? should we require picture_url, or allow Foodie to upload image directly? (TBD)| no    | yes      |
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


## Payment
- We believe we should not need a payment model to even temporarily store payment information
- This will depend on what Stripe API requires - ideally we don't want to handle payment info directly for security/liability reasons (and let alone storing it)

