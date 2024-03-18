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


Category = Literal["ADVERTISING_AND_MARKETING", "GROCERY", "TELEPHONY", "OFFICE_SUPPLIES", "PRIVATE_AIR_TRAVEL", "CLOTHING", "CAR_RENTAL", "VEHICLE_EXPENSES", "RESTAURANTS", "GAMBLING", "FLOWERS", "ELECTRONICS", "LEGAL_SERVICES", "UTILITIES", "FURNITURE", "BARS_AND_NIGHTLIFE", "LAUNDRY", "EVENT_EXPENSES", "SHIPPING", "OTHER_TRAVEL_EXPENSES", "CHARITY", "SOFTWARE_NON_RECURRING", "LODGING", "FACILITIES_EXPENSES", "SERVERS", "CONFERENCES", "FOOD_DELIVERY", "RENT", "AIRLINE_EXPENSES", "OTHER_BUSINESS_EXPENSES", "BANK_AND_FINANCIAL_FEES", "BOOKS_AND_NEWSPAPERS", "CONSULTANT_AND_CONTRACTOR", "CORPORATE_INSURANCE", "DIGITAL_GOODS", "FEES_AND_LICENSES_AND_TAXES", "GAS_AND_FUEL", "GENERAL_MERCHANDISE", "MEDICAL", "MEMBERSHIPS_AND_CLUBS", "PARKING_EXPENSES", "POLITICAL_DONATIONS", "PUBLIC_TRANSPORTATION", "RECURRING_SOFTWARE_AND_SAAS", "RIDESHARE_AND_TAXI", "TOLL_AND_BRIDGE_FEES", "TRAINING_AND_EDUCATION", "TRAVEL_WIFI"]
