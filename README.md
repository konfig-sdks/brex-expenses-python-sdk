<div align="left">

[![Visit Brex](./header.png)](https://brex.com)

# Brex<a id="brex"></a>


The Expenses API allows you to manage accounting and expenses information.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`brexexpenses.card_expenses.get_by_id`](#brexexpensescard_expensesget_by_id)
  * [`brexexpenses.card_expenses.list`](#brexexpensescard_expenseslist)
  * [`brexexpenses.card_expenses.update_expense`](#brexexpensescard_expensesupdate_expense)
  * [`brexexpenses.receipt_match.create_new_receipt_match`](#brexexpensesreceipt_matchcreate_new_receipt_match)
  * [`brexexpenses.receipt_upload.create_new_receipt`](#brexexpensesreceipt_uploadcreate_new_receipt)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Brex&serviceName=Expenses&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from brex_expenses_python_sdk import BrexExpenses, ApiException

brexexpenses = BrexExpenses(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Get an expense
    get_by_id_response = brexexpenses.card_expenses.get_by_id(
        expense_id="expense_id_example",
        expand_=["\n?expand[]=merchant&expand[]=location\n"],
    )
    print(get_by_id_response)
except ApiException as e:
    print("Exception when calling CardExpensesApi.get_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from brex_expenses_python_sdk import BrexExpenses, ApiException

brexexpenses = BrexExpenses(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Get an expense
        get_by_id_response = await brexexpenses.card_expenses.aget_by_id(
            expense_id="expense_id_example",
            expand_=["\n?expand[]=merchant&expand[]=location\n"],
        )
        print(get_by_id_response)
    except ApiException as e:
        print("Exception when calling CardExpensesApi.get_by_id: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from brex_expenses_python_sdk import BrexExpenses, ApiException

brexexpenses = BrexExpenses(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Get an expense
    get_by_id_response = brexexpenses.card_expenses.raw.get_by_id(
        expense_id="expense_id_example",
        expand_=["\n?expand[]=merchant&expand[]=location\n"],
    )
    pprint(get_by_id_response.body)
    pprint(get_by_id_response.body["id"])
    pprint(get_by_id_response.body["updated_at"])
    pprint(get_by_id_response.body["memo"])
    pprint(get_by_id_response.body["location_id"])
    pprint(get_by_id_response.body["location"])
    pprint(get_by_id_response.body["department_id"])
    pprint(get_by_id_response.body["department"])
    pprint(get_by_id_response.body["category"])
    pprint(get_by_id_response.body["merchant_id"])
    pprint(get_by_id_response.body["merchant"])
    pprint(get_by_id_response.body["receipts"])
    pprint(get_by_id_response.body["budget_id"])
    pprint(get_by_id_response.body["budget"])
    pprint(get_by_id_response.body["original_amount"])
    pprint(get_by_id_response.body["purchased_at"])
    pprint(get_by_id_response.body["status"])
    pprint(get_by_id_response.body["payment_status"])
    pprint(get_by_id_response.body["user_id"])
    pprint(get_by_id_response.body["user"])
    pprint(get_by_id_response.body["payment"])
    pprint(get_by_id_response.headers)
    pprint(get_by_id_response.status)
    pprint(get_by_id_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CardExpensesApi.get_by_id: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `brexexpenses.card_expenses.get_by_id`<a id="brexexpensescard_expensesget_by_id"></a>

Get an expense by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = brexexpenses.card_expenses.get_by_id(
    expense_id="expense_id_example",
    expand_=["\n?expand[]=merchant&expand[]=location\n"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_id: `str`<a id="expense_id-str"></a>

##### expand_: List[`str`]<a id="expand_-liststr"></a>

Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

#### 🔄 Return<a id="🔄-return"></a>

[`ExpandableExpense`](./brex_expenses_python_sdk/pydantic/expandable_expense.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/card/{expense_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexexpenses.card_expenses.list`<a id="brexexpensescard_expenseslist"></a>

List expenses under the same account. Admin and bookkeeper have access to any expense, and regular users can only access their own.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = brexexpenses.card_expenses.list(
    expand_=["\n?expand[]=merchant&expand[]=location\n"],
    user_id_=["string_example"],
    parent_expense_id_=["string_example"],
    budget_id_=["string_example"],
    status_=["string_example"],
    payment_status_=["string_example"],
    purchased_at_start="\n2023-01-01T23:59:59.999\n",
    purchased_at_end="\n2023-01-10T23:59:59.999\n",
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expand_: List[`str`]<a id="expand_-liststr"></a>

Get additional details for the expense, e.g. merchant mcc code, by passing in `expand[]=merchant`. Query parameters include `location`, `department`, `merchant`, `receipts.download_uris`, `user`, `budget` and `payment`.

##### user_id_: List[`str`]<a id="user_id_-liststr"></a>

Get expenses belong to provided user(s).

##### parent_expense_id_: List[`str`]<a id="parent_expense_id_-liststr"></a>

Get itemized expenses belong to provided parent expenses ID(s).

##### budget_id_: List[`str`]<a id="budget_id_-liststr"></a>

##### status_: List[[`ExpenseStatus`](./brex_expenses_python_sdk/type/expense_status.py)]<a id="status_-listexpensestatusbrex_expenses_python_sdktypeexpense_statuspy"></a>

##### payment_status_: List[[`ExpensePaymentStatus`](./brex_expenses_python_sdk/type/expense_payment_status.py)]<a id="payment_status_-listexpensepaymentstatusbrex_expenses_python_sdktypeexpense_payment_statuspy"></a>

##### purchased_at_start: `Optional[datetime]`<a id="purchased_at_start-optionaldatetime"></a>

 Shows only expenses with a `purchased_at` on or after this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999 

##### purchased_at_end: `Optional[datetime]`<a id="purchased_at_end-optionaldatetime"></a>

 Shows only expenses with a `purchased_at` on or before this date-time. This parameter is the date-time notation as defined by [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6), e.g. 2022-11-12T23:59:59.999 

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

 The cursor to use for pagination. This is the `next_cursor` value returned from the previous response. 

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageExpandableExpense`](./brex_expenses_python_sdk/pydantic/page_expandable_expense.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/card` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexexpenses.card_expenses.update_expense`<a id="brexexpensescard_expensesupdate_expense"></a>

Update an expense. Admin and bookkeeper have access to any expense, and regular users can only access their own.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_expense_response = brexexpenses.card_expenses.update_expense(
    expense_id="expense_id_example",
    memo="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_id: `str`<a id="expense_id-str"></a>

##### memo: `Optional[str]`<a id="memo-optionalstr"></a>

Expense memo.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateExpenseRequest`](./brex_expenses_python_sdk/type/update_expense_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Expense`](./brex_expenses_python_sdk/pydantic/expense.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/card/{expense_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexexpenses.receipt_match.create_new_receipt_match`<a id="brexexpensesreceipt_matchcreate_new_receipt_match"></a>


The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_receipt_match_response = brexexpenses.receipt_match.create_new_receipt_match(
    receipt_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### receipt_name: `str`<a id="receipt_name-str"></a>

The name of the receipt (with the file extension). It will be used in the matching result email.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReceiptMatchRequest`](./brex_expenses_python_sdk/type/receipt_match_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateAsyncFileUploadResponse`](./brex_expenses_python_sdk/pydantic/create_async_file_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/card/receipt_match` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexexpenses.receipt_upload.create_new_receipt`<a id="brexexpensesreceipt_uploadcreate_new_receipt"></a>


The `uri` will be a pre-signed S3 URL allowing you to upload the receipt securely. This URL can only be used for a `PUT` operation and expires 30 minutes after its creation. Once your upload is complete, we will try to match the receipt with existing expenses.

Refer to these [docs](https://docs.aws.amazon.com/AmazonS3/latest/dev/PresignedUrlUploadObject.html) on how to upload to this pre-signed S3 URL. We highly recommend using one of AWS SDKs if they're available for your language to upload these files.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_receipt_response = brexexpenses.receipt_upload.create_new_receipt(
    receipt_name="string_example",
    expense_id="expense_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### receipt_name: `str`<a id="receipt_name-str"></a>

The name of the receipt (with the file extension).

##### expense_id: `str`<a id="expense_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ReceiptUploadRequest`](./brex_expenses_python_sdk/type/receipt_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateAsyncFileUploadResponse`](./brex_expenses_python_sdk/pydantic/create_async_file_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/expenses/card/{expense_id}/receipt_upload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
