"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apierroraccountinactive import APIErrorAccountInactive
from .apierrorunauthorized import APIErrorUnauthorized
from .filesystem import Filesystem, FilesystemTypedDict
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from lambda_cloud_sdk import utils
from lambda_cloud_sdk.types import BaseModel
from lambda_cloud_sdk.utils import FieldMetadata, SecurityMetadata
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListFilesystemsSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    bearer_auth: NotRequired[str]


class ListFilesystemsSecurity(BaseModel):
    basic_auth: Annotated[
        Optional[SchemeBasicAuth],
        FieldMetadata(
            security=SecurityMetadata(scheme=True, scheme_type="http", sub_type="basic")
        ),
    ] = None

    bearer_auth: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ] = None


class ListFilesystemsFilesystemsResponseResponseBodyData(BaseModel):
    error: APIErrorAccountInactive


class ListFilesystemsFilesystemsResponseResponseBody(Exception):
    r"""Forbidden"""

    data: ListFilesystemsFilesystemsResponseResponseBodyData

    def __init__(self, data: ListFilesystemsFilesystemsResponseResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, ListFilesystemsFilesystemsResponseResponseBodyData
        )


class ListFilesystemsFilesystemsResponseBodyData(BaseModel):
    error: APIErrorUnauthorized


class ListFilesystemsFilesystemsResponseBody(Exception):
    r"""Unauthorized"""

    data: ListFilesystemsFilesystemsResponseBodyData

    def __init__(self, data: ListFilesystemsFilesystemsResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ListFilesystemsFilesystemsResponseBodyData)


class ListFilesystemsResponseBodyTypedDict(TypedDict):
    r"""OK"""

    data: List[FilesystemTypedDict]


class ListFilesystemsResponseBody(BaseModel):
    r"""OK"""

    data: List[Filesystem]
