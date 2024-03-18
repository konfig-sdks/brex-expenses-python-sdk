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

from brex_expenses_python_sdk.type.receipt_download_uris import ReceiptDownloadUris

class RequiredReceipt(TypedDict):
    # The unique identifier for the receipt.
    id: str

class OptionalReceipt(TypedDict, total=False):
    download_uris: ReceiptDownloadUris

class Receipt(RequiredReceipt, OptionalReceipt):
    pass
