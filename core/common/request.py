import inspect
import json

import lemoncheesecake.api as lcc
import requests


def print_request_details(url, headers, params=None, data=None, description=None):
    caller_function_name = inspect.stack()[1][3]
    if description is not None:
        lcc.log_info("{} - {} request to {}".format(description, caller_function_name.upper(), url))
    else:
        lcc.log_info("{} request to {}".format(caller_function_name.upper(), url))
    lcc.log_info("Headers: {}".format(json.dumps(headers, indent=2)))
    if caller_function_name is "get":
        lcc.log_info("Params: {}".format(json.dumps(params, indent=2)))
    elif caller_function_name in ["post", "put", "patch"]:
        lcc.log_info("Payload: {}".format(json.dumps(json.loads(data), indent=2)))


def print_response_details(response):
    lcc.log_info("Response code: {}".format(response.status_code))
    lcc.log_info("Response body: {}".format(json.dumps(json.loads(response.text), indent=2)))


def get(url, headers, params=None, description=None):
    print_request_details(url=url, headers=headers, params=params, description=description)
    response = requests.get(url=url, params=params, headers=headers)
    print_response_details(response)
    return response


def post(url, data, headers, description=None):
    print_request_details(url=url, headers=headers, data=data, description=description)
    response = requests.post(url=url, data=data, headers=headers)
    print_response_details(response)
    return response


def put(url, data, headers, credentials=None, description=None):
    print_request_details(url=url, headers=headers, data=data, description=description)
    if credentials is None:
        response = requests.put(url=url, data=data, headers=headers)
    else:
        response = requests.put(url=url, data=data, headers=headers, auth=credentials)
    print_response_details(response)
    return response


def patch(url, data, headers, description=None):
    print_request_details(url=url, headers=headers, data=data, description=description)
    response = requests.patch(url=url, data=data, headers=headers)
    print_response_details(response)
    return response


def delete(url, headers, description=None):
    print_request_details(url=url, headers=headers, description=description)
    response = requests.delete(url=url, headers=headers)
    print_response_details(response)
    return response
