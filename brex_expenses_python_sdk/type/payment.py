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

from brex_expenses_python_sdk.type.payment_instrument import PaymentInstrument

class RequiredPayment(TypedDict):
    # Unique ID for the payment.
    id: str

    payment_instrument: PaymentInstrument

class OptionalPayment(TypedDict, total=False):
    pass

class Payment(RequiredPayment, OptionalPayment):
    pass
