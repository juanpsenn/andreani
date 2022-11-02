import typing

import requests
from requests.auth import HTTPBasicAuth

from andreani.http.client import HttpClient

from .constants import BASE_URLS as URLS
from .serializers import *
from .utils import *
from .exceptions import AndreaniException


class SDK:
    sandbox: bool
    url: str
    token: str

    def __init__(self, sandbox=False):
        self.sandbox = sandbox
        self.url = URLS["test"] if sandbox else URLS["prod"]

    def login(
        self, username: str, password: str
    ) -> typing.Optional[LoginResponse]:
        endpoint = self.url + "/login"
        response = requests.get(
            url=endpoint,
            auth=HTTPBasicAuth(username, password),
        )
        if response.status_code == 200:
            response = serialize_login_repsonse(response.json())
            self.token = response.token
            return response
        raise AndreaniException(response.text)

    def estimate_price(
        self,
        postalcode: str,
        contract: str,
        client: str,
        office: str,
        order: Order,
    ) -> typing.Optional[FeesResponse]:
        endpoint = self.url + "/v1/tarifas"
        params = serialize_fees_params(
            postalcode,
            contract,
            client,
            office,
            order,
        )
        response = requests.get(url=endpoint, params=params)
        if response.status_code <= 299:
            return serialize_fees_response(response.json())
        raise AndreaniException(response.text)

    def submit_shipment(self, shipment: Shipment):
        endpoint = self.url + "/v2/ordenes-de-envio/"
        data = serialize_submit_shipment_data(shipment)
        headers = {
            "Content-Type": "application/json",
            "x-authorization-token": self.token,
        }
        response = requests.post(endpoint, data=data, headers=headers)
        return response
