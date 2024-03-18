import typing_extensions

from brex_expenses_python_sdk.paths import PathValues
from brex_expenses_python_sdk.apis.paths.v1_expenses_card import V1ExpensesCard
from brex_expenses_python_sdk.apis.paths.v1_expenses_card_receipt_match import V1ExpensesCardReceiptMatch
from brex_expenses_python_sdk.apis.paths.v1_expenses_card_expense_id import V1ExpensesCardExpenseId
from brex_expenses_python_sdk.apis.paths.v1_expenses_card_expense_id_receipt_upload import V1ExpensesCardExpenseIdReceiptUpload

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_EXPENSES_CARD: V1ExpensesCard,
        PathValues.V1_EXPENSES_CARD_RECEIPT_MATCH: V1ExpensesCardReceiptMatch,
        PathValues.V1_EXPENSES_CARD_EXPENSE_ID: V1ExpensesCardExpenseId,
        PathValues.V1_EXPENSES_CARD_EXPENSE_ID_RECEIPT_UPLOAD: V1ExpensesCardExpenseIdReceiptUpload,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_EXPENSES_CARD: V1ExpensesCard,
        PathValues.V1_EXPENSES_CARD_RECEIPT_MATCH: V1ExpensesCardReceiptMatch,
        PathValues.V1_EXPENSES_CARD_EXPENSE_ID: V1ExpensesCardExpenseId,
        PathValues.V1_EXPENSES_CARD_EXPENSE_ID_RECEIPT_UPLOAD: V1ExpensesCardExpenseIdReceiptUpload,
    }
)
