# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from brex_expenses_python_sdk import schemas  # noqa: F401


class Category(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The category of expenses.
    """


    class MetaOapg:
        enum_value_to_name = {
            "ADVERTISING_AND_MARKETING": "ADVERTISING_AND_MARKETING",
            "GROCERY": "GROCERY",
            "TELEPHONY": "TELEPHONY",
            "OFFICE_SUPPLIES": "OFFICE_SUPPLIES",
            "PRIVATE_AIR_TRAVEL": "PRIVATE_AIR_TRAVEL",
            "CLOTHING": "CLOTHING",
            "CAR_RENTAL": "CAR_RENTAL",
            "VEHICLE_EXPENSES": "VEHICLE_EXPENSES",
            "RESTAURANTS": "RESTAURANTS",
            "GAMBLING": "GAMBLING",
            "FLOWERS": "FLOWERS",
            "ELECTRONICS": "ELECTRONICS",
            "LEGAL_SERVICES": "LEGAL_SERVICES",
            "UTILITIES": "UTILITIES",
            "FURNITURE": "FURNITURE",
            "BARS_AND_NIGHTLIFE": "BARS_AND_NIGHTLIFE",
            "LAUNDRY": "LAUNDRY",
            "EVENT_EXPENSES": "EVENT_EXPENSES",
            "SHIPPING": "SHIPPING",
            "OTHER_TRAVEL_EXPENSES": "OTHER_TRAVEL_EXPENSES",
            "CHARITY": "CHARITY",
            "SOFTWARE_NON_RECURRING": "SOFTWARE_NON_RECURRING",
            "LODGING": "LODGING",
            "FACILITIES_EXPENSES": "FACILITIES_EXPENSES",
            "SERVERS": "SERVERS",
            "CONFERENCES": "CONFERENCES",
            "FOOD_DELIVERY": "FOOD_DELIVERY",
            "RENT": "RENT",
            "AIRLINE_EXPENSES": "AIRLINE_EXPENSES",
            "OTHER_BUSINESS_EXPENSES": "OTHER_BUSINESS_EXPENSES",
            "BANK_AND_FINANCIAL_FEES": "BANK_AND_FINANCIAL_FEES",
            "BOOKS_AND_NEWSPAPERS": "BOOKS_AND_NEWSPAPERS",
            "CONSULTANT_AND_CONTRACTOR": "CONSULTANT_AND_CONTRACTOR",
            "CORPORATE_INSURANCE": "CORPORATE_INSURANCE",
            "DIGITAL_GOODS": "DIGITAL_GOODS",
            "FEES_AND_LICENSES_AND_TAXES": "FEES_AND_LICENSES_AND_TAXES",
            "GAS_AND_FUEL": "GAS_AND_FUEL",
            "GENERAL_MERCHANDISE": "GENERAL_MERCHANDISE",
            "MEDICAL": "MEDICAL",
            "MEMBERSHIPS_AND_CLUBS": "MEMBERSHIPS_AND_CLUBS",
            "PARKING_EXPENSES": "PARKING_EXPENSES",
            "POLITICAL_DONATIONS": "POLITICAL_DONATIONS",
            "PUBLIC_TRANSPORTATION": "PUBLIC_TRANSPORTATION",
            "RECURRING_SOFTWARE_AND_SAAS": "RECURRING_SOFTWARE_AND_SAAS",
            "RIDESHARE_AND_TAXI": "RIDESHARE_AND_TAXI",
            "TOLL_AND_BRIDGE_FEES": "TOLL_AND_BRIDGE_FEES",
            "TRAINING_AND_EDUCATION": "TRAINING_AND_EDUCATION",
            "TRAVEL_WIFI": "TRAVEL_WIFI",
        }
    
    @schemas.classproperty
    def ADVERTISING_AND_MARKETING(cls):
        return cls("ADVERTISING_AND_MARKETING")
    
    @schemas.classproperty
    def GROCERY(cls):
        return cls("GROCERY")
    
    @schemas.classproperty
    def TELEPHONY(cls):
        return cls("TELEPHONY")
    
    @schemas.classproperty
    def OFFICE_SUPPLIES(cls):
        return cls("OFFICE_SUPPLIES")
    
    @schemas.classproperty
    def PRIVATE_AIR_TRAVEL(cls):
        return cls("PRIVATE_AIR_TRAVEL")
    
    @schemas.classproperty
    def CLOTHING(cls):
        return cls("CLOTHING")
    
    @schemas.classproperty
    def CAR_RENTAL(cls):
        return cls("CAR_RENTAL")
    
    @schemas.classproperty
    def VEHICLE_EXPENSES(cls):
        return cls("VEHICLE_EXPENSES")
    
    @schemas.classproperty
    def RESTAURANTS(cls):
        return cls("RESTAURANTS")
    
    @schemas.classproperty
    def GAMBLING(cls):
        return cls("GAMBLING")
    
    @schemas.classproperty
    def FLOWERS(cls):
        return cls("FLOWERS")
    
    @schemas.classproperty
    def ELECTRONICS(cls):
        return cls("ELECTRONICS")
    
    @schemas.classproperty
    def LEGAL_SERVICES(cls):
        return cls("LEGAL_SERVICES")
    
    @schemas.classproperty
    def UTILITIES(cls):
        return cls("UTILITIES")
    
    @schemas.classproperty
    def FURNITURE(cls):
        return cls("FURNITURE")
    
    @schemas.classproperty
    def BARS_AND_NIGHTLIFE(cls):
        return cls("BARS_AND_NIGHTLIFE")
    
    @schemas.classproperty
    def LAUNDRY(cls):
        return cls("LAUNDRY")
    
    @schemas.classproperty
    def EVENT_EXPENSES(cls):
        return cls("EVENT_EXPENSES")
    
    @schemas.classproperty
    def SHIPPING(cls):
        return cls("SHIPPING")
    
    @schemas.classproperty
    def OTHER_TRAVEL_EXPENSES(cls):
        return cls("OTHER_TRAVEL_EXPENSES")
    
    @schemas.classproperty
    def CHARITY(cls):
        return cls("CHARITY")
    
    @schemas.classproperty
    def SOFTWARE_NON_RECURRING(cls):
        return cls("SOFTWARE_NON_RECURRING")
    
    @schemas.classproperty
    def LODGING(cls):
        return cls("LODGING")
    
    @schemas.classproperty
    def FACILITIES_EXPENSES(cls):
        return cls("FACILITIES_EXPENSES")
    
    @schemas.classproperty
    def SERVERS(cls):
        return cls("SERVERS")
    
    @schemas.classproperty
    def CONFERENCES(cls):
        return cls("CONFERENCES")
    
    @schemas.classproperty
    def FOOD_DELIVERY(cls):
        return cls("FOOD_DELIVERY")
    
    @schemas.classproperty
    def RENT(cls):
        return cls("RENT")
    
    @schemas.classproperty
    def AIRLINE_EXPENSES(cls):
        return cls("AIRLINE_EXPENSES")
    
    @schemas.classproperty
    def OTHER_BUSINESS_EXPENSES(cls):
        return cls("OTHER_BUSINESS_EXPENSES")
    
    @schemas.classproperty
    def BANK_AND_FINANCIAL_FEES(cls):
        return cls("BANK_AND_FINANCIAL_FEES")
    
    @schemas.classproperty
    def BOOKS_AND_NEWSPAPERS(cls):
        return cls("BOOKS_AND_NEWSPAPERS")
    
    @schemas.classproperty
    def CONSULTANT_AND_CONTRACTOR(cls):
        return cls("CONSULTANT_AND_CONTRACTOR")
    
    @schemas.classproperty
    def CORPORATE_INSURANCE(cls):
        return cls("CORPORATE_INSURANCE")
    
    @schemas.classproperty
    def DIGITAL_GOODS(cls):
        return cls("DIGITAL_GOODS")
    
    @schemas.classproperty
    def FEES_AND_LICENSES_AND_TAXES(cls):
        return cls("FEES_AND_LICENSES_AND_TAXES")
    
    @schemas.classproperty
    def GAS_AND_FUEL(cls):
        return cls("GAS_AND_FUEL")
    
    @schemas.classproperty
    def GENERAL_MERCHANDISE(cls):
        return cls("GENERAL_MERCHANDISE")
    
    @schemas.classproperty
    def MEDICAL(cls):
        return cls("MEDICAL")
    
    @schemas.classproperty
    def MEMBERSHIPS_AND_CLUBS(cls):
        return cls("MEMBERSHIPS_AND_CLUBS")
    
    @schemas.classproperty
    def PARKING_EXPENSES(cls):
        return cls("PARKING_EXPENSES")
    
    @schemas.classproperty
    def POLITICAL_DONATIONS(cls):
        return cls("POLITICAL_DONATIONS")
    
    @schemas.classproperty
    def PUBLIC_TRANSPORTATION(cls):
        return cls("PUBLIC_TRANSPORTATION")
    
    @schemas.classproperty
    def RECURRING_SOFTWARE_AND_SAAS(cls):
        return cls("RECURRING_SOFTWARE_AND_SAAS")
    
    @schemas.classproperty
    def RIDESHARE_AND_TAXI(cls):
        return cls("RIDESHARE_AND_TAXI")
    
    @schemas.classproperty
    def TOLL_AND_BRIDGE_FEES(cls):
        return cls("TOLL_AND_BRIDGE_FEES")
    
    @schemas.classproperty
    def TRAINING_AND_EDUCATION(cls):
        return cls("TRAINING_AND_EDUCATION")
    
    @schemas.classproperty
    def TRAVEL_WIFI(cls):
        return cls("TRAVEL_WIFI")
