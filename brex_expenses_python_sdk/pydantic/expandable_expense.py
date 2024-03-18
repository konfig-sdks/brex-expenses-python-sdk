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

from brex_expenses_python_sdk.pydantic.budget import Budget
from brex_expenses_python_sdk.pydantic.category import Category
from brex_expenses_python_sdk.pydantic.department import Department
from brex_expenses_python_sdk.pydantic.expense_payment_status import ExpensePaymentStatus
from brex_expenses_python_sdk.pydantic.expense_status import ExpenseStatus
from brex_expenses_python_sdk.pydantic.location import Location
from brex_expenses_python_sdk.pydantic.merchant import Merchant
from brex_expenses_python_sdk.pydantic.money import Money
from brex_expenses_python_sdk.pydantic.payment import Payment
from brex_expenses_python_sdk.pydantic.receipt import Receipt
from brex_expenses_python_sdk.pydantic.user import User

class ExpandableExpense(BaseModel):
    # Unique ID associated with the expense.
    id: str = Field(alias='id')

    # The last time the expense was updated.
    updated_at: datetime = Field(alias='updated_at')

    # The memo of the expense.
    memo: typing.Optional[typing.Optional[str]] = Field(None, alias='memo')

    location_id: typing.Optional[typing.Optional[str]] = Field(None, alias='location_id')

    location: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='location')

    department_id: typing.Optional[typing.Optional[str]] = Field(None, alias='department_id')

    department: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='department')

    category: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='category')

    merchant_id: typing.Optional[typing.Optional[str]] = Field(None, alias='merchant_id')

    merchant: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='merchant')

    # A list of receipts associated with the expense.
    receipts: typing.Optional[typing.Optional[typing.List[Receipt]]] = Field(None, alias='receipts')

    budget_id: typing.Optional[typing.Optional[str]] = Field(None, alias='budget_id')

    budget: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='budget')

    original_amount: typing.Optional[Money] = Field(None, alias='original_amount')

    # The time the purchase was made.
    purchased_at: typing.Optional[datetime] = Field(None, alias='purchased_at')

    status: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='status')

    payment_status: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='payment_status')

    user_id: typing.Optional[typing.Optional[str]] = Field(None, alias='user_id')

    user: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user')

    payment: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='payment')
    class Config:
        arbitrary_types_allowed = True
