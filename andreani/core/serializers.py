from decimal import Decimal

from .utils import *


def serialize_fees_params(
    postalcode: str,
    contract: str,
    client: str,
    office: str,
    order: Order,
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


def serialize_fees_response(
    http_response: dict,
) -> FeesResponse:
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
    return LoginResponse(
        token=http_response["token"],
        refresh=http_response["token"],
    )


def serialize_submit_shipment_data(shipment: Shipment):
    return {
        "contrato": shipment.contract,
        "origen": {
            "postal": {
                "codigoPostal": shipment.sender_address.postalcode,
                "calle": shipment.sender_address.street,
                "numero": shipment.sender_address.number,
                "localidad": shipment.sender_address.province,
            },
            "sucursal": {"id": shipment.sender_office},
        },
        "destino": {
            "postal": {
                "codigoPostal": shipment.receiver_address.postalcode,
                "calle": shipment.receiver_address.street,
                "numero": shipment.receiver_address.number,
                "localidad": shipment.receiver_address.province,
            },
            "sucursal": {"id": shipment.receiver_office},
        },
        "remitente": {
            "nombreCompleto": f"{shipment.sender_info.first_name} {shipment.receiver_info.last_name}",
            "email": shipment.sender_info.email,
            "documentoTipo": shipment.sender_info.document_type,
            "documentoNumero": shipment.sender_info.document_number,
            "telefonos": [
                {
                    "tipo": 1,
                    "numero": shipment.sender_info.phone_number,
                }
            ],
        },
        "destinatario": [
            {
                "nombreCompleto": f"{shipment.receiver_info.first_name} {shipment.receiver_info.last_name}",
                "email": shipment.receiver_info.email,
                "documentoTipo": shipment.receiver_info.document_type,
                "documentoNumero": shipment.receiver_info.document_number,
                "telefonos": [
                    {
                        "tipo": 1,
                        "numero": shipment.receiver_info.phone_number,
                    }
                ],
            }
        ],
        "bultos": [
            {
                "kilos": shipment.order.weight,
                "volumenCm": shipment.order.volume,
                "valorDeclaradoConImpuestos": shipment.order.price,
            }
        ],
    }
