# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from brex_expenses_python_sdk.paths.v1_expenses_card_expense_id.get import GetByIdRaw
from brex_expenses_python_sdk.paths.v1_expenses_card.get import ListRaw
from brex_expenses_python_sdk.paths.v1_expenses_card_expense_id.put import UpdateExpenseRaw


class CardExpensesApiRaw(
    GetByIdRaw,
    ListRaw,
    UpdateExpenseRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
