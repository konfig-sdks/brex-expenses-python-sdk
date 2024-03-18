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
from pydantic import BaseModel, Field, RootModel

from brex_expenses_python_sdk.pydantic.card_payment_instrument import CardPaymentInstrument
from brex_expenses_python_sdk.pydantic.payment_instrument import PaymentInstrument

class PaymentInstrument(BaseModel):
    # The type of payment instrument.
    type: typing.Optional[Literal["CARD"]] = Field(None, alias='type')
    class Config:
        arbitrary_types_allowed = True
PaymentInstrument = typing.Union[PaymentInstrument]
