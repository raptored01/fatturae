# -*- coding: utf-8 -*-
# flake8:noqa
# isort:skip_file
# vim:et:ft=python:nowrap:sts=4:sw=4:ts=4
##############################################################################
# Note: Generated by soapfish.wsdl2py at 2019-01-05 23:44:43.349611
#       Try to avoid editing it if you might need to regenerate it.
##############################################################################

from soapfish import soap, xsd

BaseHeader = xsd.ComplexType

##############################################################################
# Schemas


# http://www.fatturapa.gov.it/sdi/ws/trasmissione/v1.0/types


class IdentificativoSdI_Type(xsd.Integer):
    pass


class NomeFile_Type(xsd.String):
    pattern = r"[a-zA-Z0-9_\.]{9,50}"


class ErroreInvio_Type(xsd.String):
    enumeration = ["EI01", "EI02", "EI03"]


class FileSdIBase_Type(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    NomeFile = xsd.Element(NomeFile_Type)
    File = xsd.Element(xsd.Base64Binary)

    @classmethod
    def create(cls, NomeFile, File):
        instance = cls()
        instance.NomeFile = NomeFile
        instance.File = File
        return instance


class FileSdI_Type(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    IdentificativoSdI = xsd.Element(IdentificativoSdI_Type)
    NomeFile = xsd.Element(NomeFile_Type)
    File = xsd.Element(xsd.Base64Binary)

    @classmethod
    def create(cls, IdentificativoSdI, NomeFile, File):
        instance = cls()
        instance.IdentificativoSdI = IdentificativoSdI
        instance.NomeFile = NomeFile
        instance.File = File
        return instance


class RispostaSdIRiceviFile_Type(xsd.ComplexType):
    INHERITANCE = None
    INDICATOR = xsd.Sequence
    IdentificativoSdI = xsd.Element(IdentificativoSdI_Type)
    DataOraRicezione = xsd.Element(xsd.DateTime)
    Errore = xsd.Element(ErroreInvio_Type, minOccurs=0)

    @classmethod
    def create(cls, IdentificativoSdI, DataOraRicezione):
        instance = cls()
        instance.IdentificativoSdI = IdentificativoSdI
        instance.DataOraRicezione = DataOraRicezione
        return instance


Schema_446e4 = xsd.Schema(
    imports=[],
    includes=[],
    targetNamespace="http://www.fatturapa.gov.it/sdi/ws/trasmissione/v1.0/types",
    elementFormDefault="unqualified",
    simpleTypes=[IdentificativoSdI_Type, NomeFile_Type, ErroreInvio_Type],
    attributeGroups=[],
    groups=[],
    complexTypes=[FileSdIBase_Type, FileSdI_Type, RispostaSdIRiceviFile_Type],
    elements={
        "fileSdIAccoglienza": xsd.Element(FileSdIBase_Type),
        "fileSdI": xsd.Element(FileSdI_Type),
        "rispostaSdIRiceviFile": xsd.Element(RispostaSdIRiceviFile_Type),
        "ricevutaConsegna": xsd.Element(FileSdI_Type),
        "notificaMancataConsegna": xsd.Element(FileSdI_Type),
        "notificaScarto": xsd.Element(FileSdI_Type),
        "notificaEsito": xsd.Element(FileSdI_Type),
        "notificaDecorrenzaTermini": xsd.Element(FileSdI_Type),
        "AttestazioneTrasmissioneFattura": xsd.Element(FileSdI_Type),
    },
)


##############################################################################
# Operations


def RicevutaConsegna(request, ricevutaConsegna):
    # TODO: Put your implementation here.

    pass


def NotificaMancataConsegna(request, notificaMancataConsegna):
    # TODO: Put your implementation here.

    pass


def NotificaScarto(request, notificaScarto):
    # TODO: Put your implementation here.

    pass


def NotificaEsito(request, notificaEsito):
    # TODO: Put your implementation here.

    pass


def NotificaDecorrenzaTermini(request, notificaDecorrenzaTermini):
    # TODO: Put your implementation here.

    pass


def AttestazioneTrasmissioneFattura(request, attestazioneTrasmissioneFattura):
    # TODO: Put your implementation here.

    return None


##############################################################################
# Methods


RicevutaConsegna_method = xsd.Method(
    function=RicevutaConsegna,
    soapAction="http://www.fatturapa.it/TrasmissioneFatture/RicevutaConsegna",
    input="ricevutaConsegna",
    output="xsd.String",
    inputPartName="ricevuta",
    operationName="RicevutaConsegna",
)


NotificaMancataConsegna_method = xsd.Method(
    function=NotificaMancataConsegna,
    soapAction="http://www.fatturapa.it/TrasmissioneFatture/NotificaMancataConsegna",
    input="notificaMancataConsegna",
    inputPartName="mancataConsegna",
    operationName="NotificaMancataConsegna",
)


NotificaScarto_method = xsd.Method(
    function=NotificaScarto,
    soapAction="http://www.fatturapa.it/TrasmissioneFatture/NotificaScarto",
    input="notificaScarto",
    inputPartName="scarto",
    operationName="NotificaScarto",
)


NotificaEsito_method = xsd.Method(
    function=NotificaEsito,
    soapAction="http://www.fatturapa.it/TrasmissioneFatture/NotificaEsito",
    input="notificaEsito",
    inputPartName="esito",
    operationName="NotificaEsito",
)


NotificaDecorrenzaTermini_method = xsd.Method(
    function=NotificaDecorrenzaTermini,
    soapAction="http://www.fatturapa.it/TrasmissioneFatture/NotificaDecorrenzaTermini",
    input="notificaDecorrenzaTermini",
    inputPartName="decorrenzaTermini",
    operationName="NotificaDecorrenzaTermini",
)


AttestazioneTrasmissioneFattura_method = xsd.Method(
    function=AttestazioneTrasmissioneFattura,
    soapAction="http://www.fatturapa.it/TrasmissioneFatture/AttestazioneTrasmissioneFattura",
    input="AttestazioneTrasmissioneFattura",
    inputPartName="AttestazioneTrasmissioneFattura",
    operationName="AttestazioneTrasmissioneFattura",
)


##############################################################################
# SOAP Service


TrasmissioneFatture_port_SERVICE = soap.Service(
    name="TrasmissioneFatture_port",
    targetNamespace="http://www.fatturapa.gov.it/sdi/ws/trasmissione/v1.0",
    location="${scheme}://${host}/TrasmissioneFatture",
    schemas=[Schema_446e4],
    version=soap.SOAPVersion.SOAP11,
    methods=[
        RicevutaConsegna_method,
        NotificaMancataConsegna_method,
        NotificaScarto_method,
        NotificaEsito_method,
        NotificaDecorrenzaTermini_method,
        AttestazioneTrasmissioneFattura_method,
    ],
)


##############################################################################


from soapfish.django_ import django_dispatcher

dispatcher = django_dispatcher(TrasmissioneFatture_port_SERVICE)