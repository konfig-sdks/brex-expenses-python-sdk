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


class RequiredUpdateExpenseRequest(TypedDict):
    pass

class OptionalUpdateExpenseRequest(TypedDict, total=False):
    # Expense memo.
    memo: typing.Optional[str]

class UpdateExpenseRequest(RequiredUpdateExpenseRequest, OptionalUpdateExpenseRequest):
    pass
