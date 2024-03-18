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

from brex_expenses_python_sdk.type.budget import Budget
from brex_expenses_python_sdk.type.category import Category
from brex_expenses_python_sdk.type.department import Department
from brex_expenses_python_sdk.type.expense_payment_status import ExpensePaymentStatus
from brex_expenses_python_sdk.type.expense_status import ExpenseStatus
from brex_expenses_python_sdk.type.location import Location
from brex_expenses_python_sdk.type.merchant import Merchant
from brex_expenses_python_sdk.type.money import Money
from brex_expenses_python_sdk.type.payment import Payment
from brex_expenses_python_sdk.type.receipt import Receipt
from brex_expenses_python_sdk.type.user import User

class RequiredExpandableExpense(TypedDict):
    # Unique ID associated with the expense.
    id: str

    # The last time the expense was updated.
    updated_at: datetime

class OptionalExpandableExpense(TypedDict, total=False):
    # The memo of the expense.
    memo: typing.Optional[str]

    location_id: typing.Optional[str]

    location: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    department_id: typing.Optional[str]

    department: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    category: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    merchant_id: typing.Optional[str]

    merchant: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # A list of receipts associated with the expense.
    receipts: typing.Optional[typing.List[Receipt]]

    budget_id: typing.Optional[str]

    budget: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    original_amount: Money

    # The time the purchase was made.
    purchased_at: datetime

    status: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    payment_status: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    user_id: typing.Optional[str]

    user: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    payment: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class ExpandableExpense(RequiredExpandableExpense, OptionalExpandableExpense):
    pass
