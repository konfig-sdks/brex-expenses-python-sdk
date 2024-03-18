# coding: utf-8
"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import typing
import inspect
from datetime import date, datetime
from brex_expenses_python_sdk.client_custom import ClientCustom
from brex_expenses_python_sdk.configuration import Configuration
from brex_expenses_python_sdk.api_client import ApiClient
from brex_expenses_python_sdk.type_util import copy_signature
from brex_expenses_python_sdk.apis.tags.card_expenses_api import CardExpensesApi
from brex_expenses_python_sdk.apis.tags.receipt_match_api import ReceiptMatchApi
from brex_expenses_python_sdk.apis.tags.receipt_upload_api import ReceiptUploadApi



class BrexExpenses(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.card_expenses: CardExpensesApi = CardExpensesApi(api_client)
        self.receipt_match: ReceiptMatchApi = ReceiptMatchApi(api_client)
        self.receipt_upload: ReceiptUploadApi = ReceiptUploadApi(api_client)
