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


class RequiredDepartment(TypedDict):
    # The unique identifier for the department.
    id: str

    # The name of the department.
    name: str

class OptionalDepartment(TypedDict, total=False):
    pass

class Department(RequiredDepartment, OptionalDepartment):
    pass
