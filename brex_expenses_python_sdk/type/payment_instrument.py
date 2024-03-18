# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from brex_expenses_python_sdk.type.card_payment_instrument import CardPaymentInstrument
from brex_expenses_python_sdk.type.payment_instrument import PaymentInstrument

class RequiredPaymentInstrument(TypedDict):
    pass

class OptionalPaymentInstrument(TypedDict, total=False):
    # The type of payment instrument.
    type: str

class PaymentInstrument(RequiredPaymentInstrument, OptionalPaymentInstrument):
    pass
PaymentInstrument = typing.Union[PaymentInstrument]
