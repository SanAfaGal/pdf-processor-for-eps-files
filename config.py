KEYWORDS = {
    "FACTURA": ["PERIODO FACTURADO", "FACTURA DE VENTA ELECTRONICA", "FACTURA ELECTRONICA DE VENTA"],
    "EPICRISIS": ["HISTORIA ELECTRONICA", "RESUMEN EPICRISIS"],
    "BITACORA": ["FORMATO DE BITACORA DE REMISIONES"],
    "RESOLUCION": ["RESOLUCION NO", "TRASLADO ASISTENCIAL", "PARAGRAFO"],
    "AUTORIZACION": ["CONSULTA DEL ESTADO DE AFILIACION",
                     "AUTORIZAR OTROS SERVICIOS", "SOLICITUD AUTORIZACION",
                     "OFVPERFILIIPS", "DIRECCIONAMIENTO"],
    "ORDEN_MEDICA": ["ORDENACION DE PROCEDIMIENTOS", "ORDENES MEDICAS",
                     "ORDEN MEDICA DE EGRESO", "MEDICO QUE ORDENA"],
    "COMPROBANTE": ["COMPROBANTE DE RECIBIDO DE SERVICIOS MEDICOS", "CONSTANCIA DE SERVICIOS RECIBIDOS",
                    "CERTIFICACION DE PRESTACION DE SERVICIOS", "SERVICIOS DE CONSULTA EXTERNA",
                    "SERVICIOS DE ODONTOLOGIA"],
    "RESULTADOS": ["RX", "CURACIONES", "ELECTROCARDIOGRAMA", "MEDICO RADIOLOGO"],
    "ADRES": ["ADRES"],
}

COMPOSITIONS = {
    "SERVICIOS_AMBULANCIA": KEYWORDS["BITACORA"] + KEYWORDS["RESOLUCION"],
    "VALIDACION_DERECHOS": KEYWORDS["AUTORIZACION"] + KEYWORDS["ADRES"],
    "DETALLE_CARGOS": KEYWORDS["COMPROBANTE"] + KEYWORDS["EPICRISIS"] +
                      KEYWORDS["AUTORIZACION"] + KEYWORDS["ORDEN_MEDICA"],
    "OTROS": KEYWORDS["AUTORIZACION"] + KEYWORDS["ADRES"]
}

EPS_CONFIG = {
    "NUEVA EPS": {
        "TYPES": {
            "FVS": KEYWORDS["FACTURA"],
            "EPI": KEYWORDS["EPICRISIS"],
            "TAP": KEYWORDS["BITACORA"],
            "OTR": COMPOSITIONS["OTROS"],
            "OPF": KEYWORDS["ORDEN_MEDICA"],
            "CRC": KEYWORDS["COMPROBANTE"],
            # "PDX": KEYWORDS["RESULTADOS"],
        },
        "FILENAME_FORMAT": "{file_type}_{NIT}_{PREFIX}{invoice}.pdf"
    },
    "SALUD TOTAL": {
        "TYPES": {
            1: KEYWORDS["FACTURA"],
            5: KEYWORDS["EPICRISIS"],
            # 7: KEYWORDS["RESULTADOS"],
            14: COMPOSITIONS["SERVICIOS_AMBULANCIA"],
            15: KEYWORDS["COMPROBANTE"],
            17: COMPOSITIONS["VALIDACION_DERECHOS"],
        },
        "FILENAME_FORMAT": "{NIT}_{PREFIX}_{invoice}_{file_type}_1.pdf"
    },
    "FOMAG": {
        "TYPES": {
            "FACTURA": KEYWORDS["FACTURA"],
            "DETALLEDECARGOS": COMPOSITIONS["DETALLE_CARGOS"],
        },
        "FILENAME_FORMAT": "{PREFFIX]{invoice}_{file_type}.pdf"
    }
}

HOSPITAL_CONFIG = {
    "NELSON RESTREPO MARTINEZ": {
        "NIT": "800125697",
    },
    "SAN ANTONIO": {
        "NIT": "890702408",
        "PREFIX": "FE",
    },
    "NUESTRA SEÑORA DEL CARMEN": {
        "NIT": "890702241",
        "PREFIX": "ELE",
    }
}
