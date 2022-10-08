from decimal import Decimal

import pytest

from andreani.core.api import SDK
from andreani.core.utils import Order


@pytest.fixture
def username():
    return "usuario_test"


@pytest.fixture
def password():
    return "DI$iKqMClEtM"


@pytest.fixture
def sdk():
    return SDK(sandbox=True)


@pytest.fixture
def simple_order():
    return Order(
        price=Decimal(1),
        weight=Decimal(1),
        width=Decimal(1),
        height=Decimal(1),
        length=Decimal(1),
    )
