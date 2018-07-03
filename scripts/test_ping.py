import requests

from core.common.header import Header
from core.conf.environments.config import get_config_object

config = get_config_object()
TYPICODE_PING = config.TYPICODE_BASE_URL + 'ping/'
ping_endpoints = [TYPICODE_PING]
print("Checking {}".format(ping_endpoints))
headers = Header().get_base_headers()

for endpoint in ping_endpoints:
    response = requests.get(url=endpoint, headers=headers)
    if response.status_code is not 200:
        print("{} seems down: Got response code {}".format(endpoint, response.status_code))
        exit(1)
    else:
        print("All endpoints are up!")
        exit(0)
