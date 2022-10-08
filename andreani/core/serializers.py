from decimal import Decimal

from .utils import *


def serialize_fees_params(
    postalcode: str, contract: str, client: str, office: str, order: Order
) -> dict:
    return {
        "cpDestino": postalcode,
        "contrato": contract,
        "cliente": client,
        "sucursalOrigen": office,
        "bultos[0][valorDeclarado]": order.price,
        "bultos[0][volumen]": order.volume,
        "bultos[0][kilos]": order.weight / 1000,
    }


def serialize_fees_response(http_response: dict) -> FeesResponse:
    return FeesResponse(
        messured_weight=Decimal(http_response["pesoAforado"]),
        gross_fees=Fees(
            distribution_insurance=Decimal(
                http_response["tarifaConIva"]["seguroDistribucion"]
            ),
            distribution=Decimal(http_response["tarifaConIva"]["distribucion"]),
            total=Decimal(http_response["tarifaConIva"]["total"]),
        ),
        net_fees=Fees(
            distribution_insurance=Decimal(
                http_response["tarifaSinIva"]["seguroDistribucion"]
            ),
            distribution=Decimal(http_response["tarifaSinIva"]["distribucion"]),
            total=Decimal(http_response["tarifaSinIva"]["total"]),
        ),
    )


def serialize_login_repsonse(http_response):
    return LoginResponse(token=http_response["token"], refresh=http_response["token"])
