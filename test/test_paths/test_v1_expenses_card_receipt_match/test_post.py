# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest
from unittest.mock import patch

import urllib3

import brex_expenses_python_sdk
from brex_expenses_python_sdk.paths.v1_expenses_card_receipt_match import post
from brex_expenses_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1ExpensesCardReceiptMatch(ApiTestMixin, unittest.TestCase):
    """
    V1ExpensesCardReceiptMatch unit test stubs
        Create a new receipt match
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
