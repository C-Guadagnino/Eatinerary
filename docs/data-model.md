# Data models

## Foodie
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| username        | str     | yes    | no       |
| full_name       | str     | no     | no       |
| email           | str     | yes    | no       |
| phone           | int     | yes    | no       |
| usertype        | str     | no     | no       |
| google_calendar | For.Key | yes    | no       |


## Restaurant Owner
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| username        | str     | yes    | no       |
| full_name       | str     | no     | no       |
| email           | str     | yes    | no       |
| phone           | int     | yes    | no       |
| usertype        | str     | no     | no       |
| google_calendar | For.Key | yes    | no       |
| restaurant      | For.Key | yes/no?| no       | "unsure if restaurant object is unique given some restuarants share similar info" 

## Restaurant
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| restaurant_name | str     | no     | no       |
| email           | str     | yes    | yes      |
| phone           | int     | yes    | yes      |
| location        | str     | no     | no       |
| google_calendar | For.Key | yes    | no       |
| availability    | For.Key | no     | no       | 
| picture_url     | str     | no     | no       | 
| website         | str     | no     | yes      |

## Skewered
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| restaurant      | For.Key | yes    | no       |
| foodie          | For.Key | yes    | yes      |
| create_DateTime | date    | no     | no       |
| has_visited     | bool    | no     | no       |

## Reviews
| Name            | Type    | Unique | Optional |
|-----------------|---------|--------|----------|
| title           | str     | no     | no       |
| rating          | int     | no     | no       |
| create_DateTime | date    | no     | no       |
| description     | str     | no     | no       |
| foodie          | For.Key | yes    | no       |
| restaurant      | For.Key | yes    | no       |





