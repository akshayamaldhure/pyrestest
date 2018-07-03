import json

from core.common.endpoint_constants import users
from core.common.header import Header
from core.common.request import post, get


class User(object):
    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def get_create_user_payload(self):
        create_user_payload = dict()
        create_user_payload["userName"] = self.user_name
        create_user_payload["email"] = self.email
        return create_user_payload


def create_user(base_url, payload):
    return post(url=base_url + users, data=json.dumps(payload), headers=Header().get_base_headers(),
                description="Creating user")


def get_user(base_url, user_id=None):
    if user_id:
        endpoint = users + str(user_id)
        message = "Getting user details for the user {}".format(user_id)
    else:
        endpoint = users
        message = "Getting all users"
    response = get(url=base_url + endpoint, headers=Header().get_base_headers(), description=message)
    return response
