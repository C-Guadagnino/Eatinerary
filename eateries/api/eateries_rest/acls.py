import json
import requests
from .keys import YELP_API_KEY

# Query the YELP search API by a search term and location
def get_eateries_from_yelp(location, category):
    try:
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {
            "Authorization": "Bearer %s" % YELP_API_KEY,
        }

        url_params = {
            "category": category.replace(" ", "+"),
            "location": location.replace(" ", "+"),
            "limit": 50,
        }

        response = requests.request("GET", url, headers=headers, params=url_params)

        content = json.loads(response.content)

        if "error" in content:
            return {"invalid": content["error"]["code"]}
        return content
    # handles the case when Yelp is Down
    # per Yelp Api documentation, it will return a 500 internal server error
    # https://docs.developer.yelp.com/docs/api-errors
    except:
        yelp_down_dict = {"yelp_down": "something is wrong with yelp"}
        return yelp_down_dict

def get_details_of_one_eatery(yelp_id):
    url = "https://api.yelp.com/v3/businesses/" + yelp_id

    headers = {
        "Authorization": "Bearer %s" % YELP_API_KEY,
    }

    response = requests.request("GET", url, headers=headers)
    content = json.loads(response.content)

    return content
