import typing

import requests
from requests.auth import HTTPBasicAuth

from andreani.http.client import HttpClient

from .constants import BASE_URLS as URLS
from .serializers import *
from .utils import *


class SDK:
    sandbox: bool
    url: str

    def __init__(self, sandbox=False):
        self.sandbox = sandbox
        self.url = URLS["test"] if sandbox else URLS["prod"]

    def login(self, username: str, password: str) -> typing.Optional[LoginResponse]:
        endpoint = self.url + "/login"
        response = requests.get(url=endpoint, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            return serialize_login_repsonse(response.json())
        return None

    def estimate_price(
        self, postalcode: str, contract: str, client: str, office: str, order: Order
    ) -> FeesResponse:
        endpoint = self.url + "/v1/tarifas"
        params = serialize_fees_params(postalcode, contract, client, office, order)
        response = requests.get(url=endpoint, params=params)

        return serialize_fees_response(response.json())
