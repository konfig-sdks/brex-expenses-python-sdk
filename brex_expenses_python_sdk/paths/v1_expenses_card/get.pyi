# coding: utf-8

"""
    Expenses API

     The Expenses API allows you to manage accounting and expenses information. 

    The version of the OpenAPI document: 0.1
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from brex_expenses_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from brex_expenses_python_sdk.api_response import AsyncGeneratorResponse
from brex_expenses_python_sdk import api_client, exceptions
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

from brex_expenses_python_sdk.model.page_expandable_expense import PageExpandableExpense as PageExpandableExpenseSchema
from brex_expenses_python_sdk.model.expense_payment_status import ExpensePaymentStatus as ExpensePaymentStatusSchema
from brex_expenses_python_sdk.model.expense_status import ExpenseStatus as ExpenseStatusSchema

from brex_expenses_python_sdk.type.page_expandable_expense import PageExpandableExpense
from brex_expenses_python_sdk.type.expense_payment_status import ExpensePaymentStatus
from brex_expenses_python_sdk.type.expense_status import ExpenseStatus

from ...api_client import Dictionary
from brex_expenses_python_sdk.pydantic.page_expandable_expense import PageExpandableExpense as PageExpandableExpensePydantic
from brex_expenses_python_sdk.pydantic.expense_payment_status import ExpensePaymentStatus as ExpensePaymentStatusPydantic
from brex_expenses_python_sdk.pydantic.expense_status import ExpenseStatus as ExpenseStatusPydantic

# Query params


class ExpandSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpandSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class UserIdSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class ParentExpenseIdSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ParentExpenseIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class BudgetIdSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        items = schemas.StrSchema


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BudgetIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class StatusSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExpenseStatus']:
            return ExpenseStatus


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StatusSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class PaymentStatusSchema(
    schemas.ListBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneTupleMixin
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExpensePaymentStatus']:
            return ExpensePaymentStatus


    def __new__(
        cls,
        *args: typing.Union[list, tuple, None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PaymentStatusSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class PurchasedAtStartSchema(
    schemas.DateTimeBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date-time'


    def __new__(
        cls,
        *args: typing.Union[None, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PurchasedAtStartSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class PurchasedAtEndSchema(
    schemas.DateTimeBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date-time'


    def __new__(
        cls,
        *args: typing.Union[None, str, datetime, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PurchasedAtEndSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class CursorSchema(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CursorSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )


class LimitSchema(
    schemas.Int32Base,
    schemas.IntBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneDecimalMixin
):


    class MetaOapg:
        format = 'int32'


    def __new__(
        cls,
        *args: typing.Union[None, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LimitSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'expand[]': typing.Union[ExpandSchema, list, tuple, None, ],
        'user_id[]': typing.Union[UserIdSchema, list, tuple, None, ],
        'parent_expense_id[]': typing.Union[ParentExpenseIdSchema, list, tuple, None, ],
        'budget_id[]': typing.Union[BudgetIdSchema, list, tuple, None, ],
        'status[]': typing.Union[StatusSchema, list, tuple, None, ],
        'payment_status[]': typing.Union[PaymentStatusSchema, list, tuple, None, ],
        'purchased_at_start': typing.Union[PurchasedAtStartSchema, None, str, datetime, ],
        'purchased_at_end': typing.Union[PurchasedAtEndSchema, None, str, datetime, ],
        'cursor': typing.Union[CursorSchema, None, str, ],
        'limit': typing.Union[LimitSchema, None, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_expand_ = api_client.QueryParameter(
    name="expand[]",
    style=api_client.ParameterStyle.FORM,
    schema=ExpandSchema,
    explode=True,
)
request_query_user_id_ = api_client.QueryParameter(
    name="user_id[]",
    style=api_client.ParameterStyle.FORM,
    schema=UserIdSchema,
    explode=True,
)
request_query_parent_expense_id_ = api_client.QueryParameter(
    name="parent_expense_id[]",
    style=api_client.ParameterStyle.FORM,
    schema=ParentExpenseIdSchema,
    explode=True,
)
request_query_budget_id_ = api_client.QueryParameter(
    name="budget_id[]",
    style=api_client.ParameterStyle.FORM,
    schema=BudgetIdSchema,
    explode=True,
)
request_query_status_ = api_client.QueryParameter(
    name="status[]",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_payment_status_ = api_client.QueryParameter(
    name="payment_status[]",
    style=api_client.ParameterStyle.FORM,
    schema=PaymentStatusSchema,
    explode=True,
)
request_query_purchased_at_start = api_client.QueryParameter(
    name="purchased_at_start",
    style=api_client.ParameterStyle.FORM,
    schema=PurchasedAtStartSchema,
    explode=True,
)
request_query_purchased_at_end = api_client.QueryParameter(
    name="purchased_at_end",
    style=api_client.ParameterStyle.FORM,
    schema=PurchasedAtEndSchema,
    explode=True,
)
request_query_cursor = api_client.QueryParameter(
    name="cursor",
    style=api_client.ParameterStyle.FORM,
    schema=CursorSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PageExpandableExpenseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PageExpandableExpense


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PageExpandableExpense


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_mapped_args(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if expand_ is not None:
            _query_params["expand[]"] = expand_
        if user_id_ is not None:
            _query_params["user_id[]"] = user_id_
        if parent_expense_id_ is not None:
            _query_params["parent_expense_id[]"] = parent_expense_id_
        if budget_id_ is not None:
            _query_params["budget_id[]"] = budget_id_
        if status_ is not None:
            _query_params["status[]"] = status_
        if payment_status_ is not None:
            _query_params["payment_status[]"] = payment_status_
        if purchased_at_start is not None:
            _query_params["purchased_at_start"] = purchased_at_start
        if purchased_at_end is not None:
            _query_params["purchased_at_end"] = purchased_at_end
        if cursor is not None:
            _query_params["cursor"] = cursor
        if limit is not None:
            _query_params["limit"] = limit
        args.query = _query_params
        return args

    async def _alist_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List expenses
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand_,
            request_query_user_id_,
            request_query_parent_expense_id_,
            request_query_budget_id_,
            request_query_status_,
            request_query_payment_status_,
            request_query_purchased_at_start,
            request_query_purchased_at_end,
            request_query_cursor,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/expenses/card',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List expenses
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_expand_,
            request_query_user_id_,
            request_query_parent_expense_id_,
            request_query_budget_id_,
            request_query_status_,
            request_query_payment_status_,
            request_query_purchased_at_start,
            request_query_purchased_at_end,
            request_query_cursor,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/expenses/card',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            expand_=expand_,
            user_id_=user_id_,
            parent_expense_id_=parent_expense_id_,
            budget_id_=budget_id_,
            status_=status_,
            payment_status_=payment_status_,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            cursor=cursor,
            limit=limit,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            expand_=expand_,
            user_id_=user_id_,
            parent_expense_id_=parent_expense_id_,
            budget_id_=budget_id_,
            status_=status_,
            payment_status_=payment_status_,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            cursor=cursor,
            limit=limit,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PageExpandableExpensePydantic:
        raw_response = await self.raw.alist(
            expand_=expand_,
            user_id_=user_id_,
            parent_expense_id_=parent_expense_id_,
            budget_id_=budget_id_,
            status_=status_,
            payment_status_=payment_status_,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            cursor=cursor,
            limit=limit,
            **kwargs,
        )
        if validate:
            return PageExpandableExpensePydantic(**raw_response.body)
        return api_client.construct_model_instance(PageExpandableExpensePydantic, raw_response.body)
    
    
    def list(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        validate: bool = False,
    ) -> PageExpandableExpensePydantic:
        raw_response = self.raw.list(
            expand_=expand_,
            user_id_=user_id_,
            parent_expense_id_=parent_expense_id_,
            budget_id_=budget_id_,
            status_=status_,
            payment_status_=payment_status_,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            cursor=cursor,
            limit=limit,
        )
        if validate:
            return PageExpandableExpensePydantic(**raw_response.body)
        return api_client.construct_model_instance(PageExpandableExpensePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            expand_=expand_,
            user_id_=user_id_,
            parent_expense_id_=parent_expense_id_,
            budget_id_=budget_id_,
            status_=status_,
            payment_status_=payment_status_,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            cursor=cursor,
            limit=limit,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        expand_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        user_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        parent_expense_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        budget_id_: typing.Optional[typing.Optional[typing.List[str]]] = None,
        status_: typing.Optional[typing.Optional[typing.List[ExpenseStatus]]] = None,
        payment_status_: typing.Optional[typing.Optional[typing.List[ExpensePaymentStatus]]] = None,
        purchased_at_start: typing.Optional[typing.Optional[datetime]] = None,
        purchased_at_end: typing.Optional[typing.Optional[datetime]] = None,
        cursor: typing.Optional[typing.Optional[str]] = None,
        limit: typing.Optional[typing.Optional[int]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            expand_=expand_,
            user_id_=user_id_,
            parent_expense_id_=parent_expense_id_,
            budget_id_=budget_id_,
            status_=status_,
            payment_status_=payment_status_,
            purchased_at_start=purchased_at_start,
            purchased_at_end=purchased_at_end,
            cursor=cursor,
            limit=limit,
        )
        return self._list_oapg(
            query_params=args.query,
        )

