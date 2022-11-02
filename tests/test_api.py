from decimal import Decimal

import pytest

from andreani.core.api import SDK
from andreani.core.utils import (
    FeesResponse,
    LoginResponse,
)


def test_login_successfully(username, password, sdk):
    auth = sdk.login(username, password)

    assert type(auth) == LoginResponse
    assert auth.token is not None


def test_estimate_price(simple_order, sdk):
    fees = sdk.estimate_price(
        "1400",
        "300006611",
        "CL0003750",
        "BAR",
        simple_order,
    )

    assert type(fees) == FeesResponse
    assert fees.messured_weight == Decimal(1)


def test_submit_shipment(shipment, username, password, sdk):
    sdk.login(username, password)
    response = sdk.submit_shipment(shipment)

    assert response.status_code == 403
