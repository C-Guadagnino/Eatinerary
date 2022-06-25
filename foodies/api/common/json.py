from json import JSONEncoder
from django.urls import NoReverseMatch
from django.db.models import QuerySet
from datetime import datetime, date, time


class TimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, time):
            return o.isoformat()
        else:
            return super().default(o)


class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()
        else:
            return super().default(o)


class DateTimeEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            return super().default(o)


class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


class ModelEncoder(
    TimeEncoder, DateEncoder, DateTimeEncoder, QuerySetEncoder, JSONEncoder
):
    encoders = {}

    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            if hasattr(o, "get_api_url"):
                try:
                    d["href"] = o.get_api_url()
                except NoReverseMatch:
                    pass
            for property in self.properties:
                # value to be added to the d dictionary after being encoded if
                # needed
                value = getattr(o, property)
                # birds-eye view motivation: this takes care of serializing a
                # list of EateryCategory objects,
                # because without 7 lines of code below, we'd get a "TypeError:
                # Object of type ManyRelatedManager is not JSON serializable"
                #
                # high-level: if value is a ManyRelatedManager/RelatedManager
                # object detail: if value has .all method and is not a QuerySet
                # (because QuerySet objects also have .all methods)
                if hasattr(value, "all") and not isinstance(value, QuerySet):
                    # store value into variable values because in this case
                    # value.all() is a list of EateryCategory objects)
                    #
                    # side note: value up to here is still a ManyRelatedManager
                    # object plus we don't want to overwrite the value variable
                    # used above
                    values = value.all()
                    # intialize value to be an empty list as a container so
                    # that we can append the encoded dictionary
                    value = []
                    # for each item (aka. EateryCategory object) in values
                    # (aka. list of EateryCategory objects)
                    for item in values:
                        # if the EateryEncoder has an "encoders" dictionary,
                        # which has "categories" as a key
                        if property in self.encoders:
                            # grab that encoder. In this case,
                            # "EateryCategoryEncoder()"
                            encoder = self.encoders[property]
                            # append (*REF A*) to the value list (which is just
                            # a container) (*REF A*) the encoded item (aka.
                            # EateryCategory) using the
                            # "EateryCategoryEncoder()"
                            value.append(encoder.default(item))
                elif property in self.encoders:
                    encoder = self.encoders[property]
                    value = encoder.default(value)
                d[property] = value
            d.update(self.get_extra_data(o))
            return d
        else:
            return super().default(o)

    def get_extra_data(self, o):
        return {}
