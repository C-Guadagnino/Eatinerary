import json
import requests
from .keys import YELP_API_KEY

# print("yelp key": YELP_API_KEY)
# businesses/search?categories=restaurant?location= + variable_here
def get_restaurants():
    url = "https://api.yelp.com/v3/businesses/search?location=" + "Philadelphia"

    headers = {
        "Authorization": "Bearer %s" % YELP_API_KEY,
    }

    # response = requests.get(url, headers=headers)
    response = requests.request("GET", url, headers=headers)

    content = json.loads(response.content)
    print("content is:", content)
    print("length of content is:", len(content["businesses"]))
    return content
    # locations = response["businesses"]

    # if locations and len(locations) > 0:
    #     return locations


# businesses/search?categories=restaurant?location= + variable_here
# Query the search API by a search term and location
def get_eateries(location, categories):
    # url = "https://api.yelp.com/v3/businesses/search?categories=" + categories + "&location=" + location
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        "Authorization": "Bearer %s" % YELP_API_KEY,
    }

    url_params = {
        "categories": categories.replace(" ", "+"),
        "location": location.replace(" ", "+"),
    }

    # response = requests.get(url, headers=headers)
    response = requests.request("GET", url, headers=headers, params=url_params)
    # response = requests.request('GET', url, headers=headers)

    content = json.loads(response.content)
    print("content is:", content)
    # print("length of content is:", len(content["businesses"]))
    return content
    # locations = response["businesses"]

    # if locations and len(locations) > 0:
    #     return locations
