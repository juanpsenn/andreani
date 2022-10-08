from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Order:
    price: Decimal
    weight: Decimal
    width: Decimal
    height: Decimal
    length: Decimal

    @property
    def volume(self):
        return self.width * self.height * self.length


@dataclass
class LoginResponse:
    token: str
    refresh: str


@dataclass
class Fees:
    distribution_insurance: Decimal
    distribution: Decimal
    total: Decimal


@dataclass
class FeesResponse:
    messured_weight: Decimal
    gross_fees: Fees
    net_fees: Fees
