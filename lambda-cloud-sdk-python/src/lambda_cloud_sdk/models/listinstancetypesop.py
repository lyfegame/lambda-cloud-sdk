"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apierroraccountinactive import APIErrorAccountInactive
from .apierrorunauthorized import APIErrorUnauthorized
from .instancetypesitem import InstanceTypesItem, InstanceTypesItemTypedDict
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from lambda_cloud_sdk import utils
from lambda_cloud_sdk.types import BaseModel
from lambda_cloud_sdk.utils import FieldMetadata, SecurityMetadata
from typing import Dict, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListInstanceTypesSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    bearer_auth: NotRequired[str]


class ListInstanceTypesSecurity(BaseModel):
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


class ListInstanceTypesInstancesResponseResponseBodyData(BaseModel):
    error: APIErrorAccountInactive


class ListInstanceTypesInstancesResponseResponseBody(Exception):
    r"""Forbidden"""

    data: ListInstanceTypesInstancesResponseResponseBodyData

    def __init__(self, data: ListInstanceTypesInstancesResponseResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, ListInstanceTypesInstancesResponseResponseBodyData
        )


class ListInstanceTypesInstancesResponseBodyData(BaseModel):
    error: APIErrorUnauthorized


class ListInstanceTypesInstancesResponseBody(Exception):
    r"""Unauthorized"""

    data: ListInstanceTypesInstancesResponseBodyData

    def __init__(self, data: ListInstanceTypesInstancesResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ListInstanceTypesInstancesResponseBodyData)


class ListInstanceTypesResponseBodyTypedDict(TypedDict):
    r"""OK"""

    data: Dict[str, InstanceTypesItemTypedDict]


class ListInstanceTypesResponseBody(BaseModel):
    r"""OK"""

    data: Dict[str, InstanceTypesItem]
