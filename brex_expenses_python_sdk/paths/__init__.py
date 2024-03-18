# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from brex_expenses_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_EXPENSES_CARD = "/v1/expenses/card"
    V1_EXPENSES_CARD_RECEIPT_MATCH = "/v1/expenses/card/receipt_match"
    V1_EXPENSES_CARD_EXPENSE_ID = "/v1/expenses/card/{expense_id}"
    V1_EXPENSES_CARD_EXPENSE_ID_RECEIPT_UPLOAD = "/v1/expenses/card/{expense_id}/receipt_upload"
