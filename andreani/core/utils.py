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
class Address:
    postalcode: str
    street: str
    number: str
    apartment: str
    floor: str
    region: str
    province: str
    country: str


@dataclass
class Person:
    first_name: str
    last_name: str
    email: str
    document_number: str
    phone_number: str
    document_type: str = "DNI"


@dataclass
class Shipment:
    contract: str
    sender_info: Person
    sender_address: Address
    sender_office: str
    receiver_info: Person
    receiver_address: Address
    receiver_office: str
    order: Order


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
