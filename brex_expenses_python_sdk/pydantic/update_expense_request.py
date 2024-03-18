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


class UpdateExpenseRequest(BaseModel):
    # Expense memo.
    memo: typing.Optional[typing.Optional[str]] = Field(None, alias='memo')
    class Config:
        arbitrary_types_allowed = True
