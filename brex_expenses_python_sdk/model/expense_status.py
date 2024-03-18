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


class ExpenseStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "DRAFT": "DRAFT",
            "SUBMITTED": "SUBMITTED",
            "APPROVED": "APPROVED",
            "OUT_OF_POLICY": "OUT_OF_POLICY",
            "VOID": "VOID",
            "CANCELED": "CANCELED",
            "SPLIT": "SPLIT",
            "SETTLED": "SETTLED",
        }
    
    @schemas.classproperty
    def DRAFT(cls):
        return cls("DRAFT")
    
    @schemas.classproperty
    def SUBMITTED(cls):
        return cls("SUBMITTED")
    
    @schemas.classproperty
    def APPROVED(cls):
        return cls("APPROVED")
    
    @schemas.classproperty
    def OUT_OF_POLICY(cls):
        return cls("OUT_OF_POLICY")
    
    @schemas.classproperty
    def VOID(cls):
        return cls("VOID")
    
    @schemas.classproperty
    def CANCELED(cls):
        return cls("CANCELED")
    
    @schemas.classproperty
    def SPLIT(cls):
        return cls("SPLIT")
    
    @schemas.classproperty
    def SETTLED(cls):
        return cls("SETTLED")