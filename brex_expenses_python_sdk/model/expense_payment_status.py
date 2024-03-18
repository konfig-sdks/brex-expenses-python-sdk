# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from brex_expenses_python_sdk import schemas  # noqa: F401


class ExpensePaymentStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "NOT_STARTED": "NOT_STARTED",
            "PROCESSING": "PROCESSING",
            "CANCELED": "CANCELED",
            "DECLINED": "DECLINED",
            "CLEARED": "CLEARED",
            "REFUNDING": "REFUNDING",
            "REFUNDED": "REFUNDED",
            "CASH_ADVANCE": "CASH_ADVANCE",
            "CREDITED": "CREDITED",
            "AWAITING_PAYMENT": "AWAITING_PAYMENT",
        }
    
    @schemas.classproperty
    def NOT_STARTED(cls):
        return cls("NOT_STARTED")
    
    @schemas.classproperty
    def PROCESSING(cls):
        return cls("PROCESSING")
    
    @schemas.classproperty
    def CANCELED(cls):
        return cls("CANCELED")
    
    @schemas.classproperty
    def DECLINED(cls):
        return cls("DECLINED")
    
    @schemas.classproperty
    def CLEARED(cls):
        return cls("CLEARED")
    
    @schemas.classproperty
    def REFUNDING(cls):
        return cls("REFUNDING")
    
    @schemas.classproperty
    def REFUNDED(cls):
        return cls("REFUNDED")
    
    @schemas.classproperty
    def CASH_ADVANCE(cls):
        return cls("CASH_ADVANCE")
    
    @schemas.classproperty
    def CREDITED(cls):
        return cls("CREDITED")
    
    @schemas.classproperty
    def AWAITING_PAYMENT(cls):
        return cls("AWAITING_PAYMENT")