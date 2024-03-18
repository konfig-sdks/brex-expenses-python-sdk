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


class Budget(BaseModel):
    # Unique ID for the Budget.
    id: str = Field(alias='id')

    # Name for the Budget.
    name: str = Field(alias='name')
    class Config:
        arbitrary_types_allowed = True
