import json
import requests
from .keys import YELP_API_KEY

# print("yelp key": YELP_API_KEY)
# businesses/search?categories=restaurant?location= + variable_here
def get_restaurants(location):
    url = "https://api.yelp.com/v3/businesses/search?location=" + location

    headers = {
        "Authorization": "Bearer %s" % YELP_API_KEY,
    }

    url_params = {"limit": 50}
    # response = requests.get(url, headers=headers)
    response = requests.request("GET", url, headers=headers, params=url_params)

    content = json.loads(response.content)
    # print("IM INSIDE OF ACLS.PY and content is:", content)
    print("length of content is:", len(content["businesses"]))
    return content
    # locations = response["businesses"]

    # if locations and len(locations) > 0:
    #     return locations


# businesses/search?categories=restaurant?location= + variable_here
# Query the search API by a search term and location
def get_eateries_from_yelp(location, categories):
    # url = "https://api.yelp.com/v3/businesses/search?categories=" + categories + "&location=" + location
    # We will handle the key errors for location mis spells in views
    try:
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {
            "Authorization": "Bearer %s" % YELP_API_KEY,
        }

        url_params = {
            "categories": categories.replace(" ", "+"),
            "location": location.replace(" ", "+"),
            "limit": 50,
        }

        # response = requests.get(url, headers=headers)
        response = requests.request("GET", url, headers=headers, params=url_params)
        # response = requests.request('GET', url, headers=headers)

        content = json.loads(response.content)
        # print("IM INSIDE OF ACLS.PY and content is:", content)
        # print("length of content is:", len(content["businesses"]))
        print("CONTENT", content)
        # if the location is bad the Yelp Api return content dictionary that holds error key
        # but if the category is bad it still returns businesses dictionary
        if "error" in content:
            return {"invalid": content["error"]["code"]}
        return content
    # handles the case when Yelp is Down
    # per Yelp Api documentation, it will return a 500 internal server error
    # https://docs.developer.yelp.com/docs/api-errors
    except:
        yelp_down_dict = {"yelp_down": "something is wrong with yelp"}
        return yelp_down_dict

    # locations = response["businesses"]

    # if locations and len(locations) > 0:
    #     return locations


def get_details_of_one_eatery(yelp_id):
    url = "https://api.yelp.com/v3/businesses/" + yelp_id

    headers = {
        "Authorization": "Bearer %s" % YELP_API_KEY,
    }

    response = requests.request("GET", url, headers=headers)

    content = json.loads(response.content)
    # print("IM INSIDE OF ACLS.PY and content is:", content)
    return content
