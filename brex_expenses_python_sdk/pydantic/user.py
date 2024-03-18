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


class User(BaseModel):
    # Unique ID for the User.
    id: str = Field(alias='id')

    # First name of the User.
    first_name: str = Field(alias='first_name')

    # Last name of the User.
    last_name: str = Field(alias='last_name')

    department_id: typing.Optional[typing.Optional[str]] = Field(None, alias='department_id')

    location_id: typing.Optional[typing.Optional[str]] = Field(None, alias='location_id')
    class Config:
        arbitrary_types_allowed = True
