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
from pydantic import BaseModel, Field, RootModel


class CreateAsyncFileUploadResponse(BaseModel):
    # The unique identifier for the request.
    id: str = Field(alias='id')

    # The pre-signed S3 link that should be used to upload the file. The maximum size accepted for this document is 50 MB. 
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
