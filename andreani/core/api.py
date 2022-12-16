import json
import typing
from decimal import Decimal

import requests
from requests.auth import HTTPBasicAuth

from .constants import BASE_URLS as URLS
from .exceptions import AndreaniException
from .serializers import (
    serialize_fees_params,
    serialize_fees_response,
    serialize_login_repsonse,
    serialize_submit_shipment_data,
    serialize_submit_shipment_response,
)
from .utils import FeesResponse, LoginResponse, Order, Shipment, SubmitShipmentResponse


class DecimalEncoder(json.JSONEncoder):
    """See https://bobbyhadz.com/blog/python-typeerror-object-of-type-decimal-is-not-json-serializable"""

    def default(self, obj):
        # 👇️ if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return float(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


class SDK:
    sandbox: bool
    url: str
    token: str

    def __init__(self, sandbox=False):
        self.sandbox = sandbox
        self.url = URLS["test"] if sandbox else URLS["prod"]

    def login(self, username: str, password: str) -> typing.Optional[LoginResponse]:
        endpoint = self.url + "/login"
        response = requests.get(
            url=endpoint,
            auth=HTTPBasicAuth(username, password),
        )
        if response.status_code == 200:
            login_response = serialize_login_repsonse(response.json())
            self.token = login_response.token
            return login_response
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

    def get_label(self, url: str):
        # NOT WORKING FIX ME
        endpoint = url
        headers = {
            "Content-Type": "application/json",
            "x-authorization-token": self.token,
        }
        response = requests.get(endpoint, headers)
        return response

    def submit_shipment(
        self, shipment: Shipment
    ) -> typing.Optional[SubmitShipmentResponse]:
        endpoint = self.url + "/v2/ordenes-de-envio"
        data = serialize_submit_shipment_data(shipment)
        headers = {
            "Content-Type": "application/json",
            "x-authorization-token": self.token,
        }
        encoded_data = json.dumps(data, cls=DecimalEncoder)

        response = requests.post(endpoint, data=encoded_data, headers=headers)
        if response.status_code <= 299:
            return serialize_submit_shipment_response(response.json())
        raise AndreaniException(response.text)
