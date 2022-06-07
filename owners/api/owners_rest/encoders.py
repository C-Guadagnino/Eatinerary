from owners_rest.models import EateryVO
from common.json import ModelEncoder

class EateryVOEncoder(ModelEncoder):
    model = EateryVO
    properties = [
        "import_href",
        "eatery_name",
        "website",
        "email",
        "phone",
        "yelp_id",
        "review_count",
        "average_rating",
        "price"
    ]