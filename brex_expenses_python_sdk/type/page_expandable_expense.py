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

from brex_expenses_python_sdk.type.expandable_expense import ExpandableExpense

class RequiredPageExpandableExpense(TypedDict):
    items: typing.List[ExpandableExpense]

class OptionalPageExpandableExpense(TypedDict, total=False):
    next_cursor: typing.Optional[str]

class PageExpandableExpense(RequiredPageExpandableExpense, OptionalPageExpandableExpense):
    pass
