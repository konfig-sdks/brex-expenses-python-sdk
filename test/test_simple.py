# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest

import os
from pprint import pprint
from brex_expenses_python_sdk import BrexExpenses

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        brexexpenses = BrexExpenses(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(brexexpenses)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
