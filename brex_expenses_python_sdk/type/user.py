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


class RequiredUser(TypedDict):
    # Unique ID for the User.
    id: str

    # First name of the User.
    first_name: str

    # Last name of the User.
    last_name: str

class OptionalUser(TypedDict, total=False):
    department_id: typing.Optional[str]

    location_id: typing.Optional[str]

class User(RequiredUser, OptionalUser):
    pass
