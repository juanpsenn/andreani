# andreani

This is a Python module that provides a class called SDK for interacting with the [Andreani API](https://developers.andreani.com/documentacion/). The SDK class has several methods that allow users to login, estimate shipping fees, retrieve shipping labels, and submit shipments to Andreani.

## SDK class:

1. `login(username: str, password: str) -> typing.Optional[LoginResponse]`: This method logs in to the Andreani API using the provided username and password. It returns a LoginResponse object if the login was successful, or raises an AndreaniException if there was an error.

2. `estimate_price(postalcode: str, contract: str, client: str, office: str, order: Order) -> typing.Optional[FeesResponse]`: This method estimates the shipping fees for a given postalcode, contract, client, office, and order. It returns a FeesResponse object if the request was successful, or raises an AndreaniException if there was an error.

3. `submit_shipment(shipment: Shipment) -> typing.Optional[SubmitShipmentResponse]`: This method submits a shipment to Andreani. It returns a SubmitShipmentResponse object if the request was successful, or raises an AndreaniException if there was an error.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This software is distributed under the MIT licence. See LICENCE for details.

Copyright (c) 2021-2022 Juan Pablo Senn <juanpsenn@gmail.com>
