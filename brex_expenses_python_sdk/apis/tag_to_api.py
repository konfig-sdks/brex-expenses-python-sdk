import typing_extensions

from brex_expenses_python_sdk.apis.tags import TagValues
from brex_expenses_python_sdk.apis.tags.card_expenses_api import CardExpensesApi
from brex_expenses_python_sdk.apis.tags.receipt_match_api import ReceiptMatchApi
from brex_expenses_python_sdk.apis.tags.receipt_upload_api import ReceiptUploadApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CARD_EXPENSES: CardExpensesApi,
        TagValues.RECEIPT_MATCH: ReceiptMatchApi,
        TagValues.RECEIPT_UPLOAD: ReceiptUploadApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CARD_EXPENSES: CardExpensesApi,
        TagValues.RECEIPT_MATCH: ReceiptMatchApi,
        TagValues.RECEIPT_UPLOAD: ReceiptUploadApi,
    }
)
