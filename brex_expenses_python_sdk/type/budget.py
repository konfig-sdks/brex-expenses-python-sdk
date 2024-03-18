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


class RequiredBudget(TypedDict):
    # Unique ID for the Budget.
    id: str

    # Name for the Budget.
    name: str

class OptionalBudget(TypedDict, total=False):
    pass

class Budget(RequiredBudget, OptionalBudget):
    pass
