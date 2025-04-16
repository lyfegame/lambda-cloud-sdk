"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apierroraccountinactive import APIErrorAccountInactive
from .apierrorinstancenotfound import APIErrorInstanceNotFound
from .apierrorunauthorized import APIErrorUnauthorized
from .instance import Instance, InstanceTypedDict
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from lambda_cloud_sdk import utils
from lambda_cloud_sdk.types import BaseModel
from lambda_cloud_sdk.utils import FieldMetadata, PathParamMetadata, SecurityMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetInstanceSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    bearer_auth: NotRequired[str]


class GetInstanceSecurity(BaseModel):
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


class GetInstanceRequestTypedDict(TypedDict):
    id: str
    r"""The unique identifier (ID) of the instance"""


class GetInstanceRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier (ID) of the instance"""


class GetInstanceInstancesResponse404ResponseBodyData(BaseModel):
    error: APIErrorInstanceNotFound


class GetInstanceInstancesResponse404ResponseBody(Exception):
    r"""Not Found"""

    data: GetInstanceInstancesResponse404ResponseBodyData

    def __init__(self, data: GetInstanceInstancesResponse404ResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, GetInstanceInstancesResponse404ResponseBodyData
        )


class GetInstanceInstancesResponseResponseBodyData(BaseModel):
    error: APIErrorAccountInactive


class GetInstanceInstancesResponseResponseBody(Exception):
    r"""Forbidden"""

    data: GetInstanceInstancesResponseResponseBodyData

    def __init__(self, data: GetInstanceInstancesResponseResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, GetInstanceInstancesResponseResponseBodyData
        )


class GetInstanceInstancesResponseBodyData(BaseModel):
    error: APIErrorUnauthorized


class GetInstanceInstancesResponseBody(Exception):
    r"""Unauthorized"""

    data: GetInstanceInstancesResponseBodyData

    def __init__(self, data: GetInstanceInstancesResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, GetInstanceInstancesResponseBodyData)


class GetInstanceResponseBodyTypedDict(TypedDict):
    r"""OK"""

    data: InstanceTypedDict
    r"""Detailed information about the instance."""


class GetInstanceResponseBody(BaseModel):
    r"""OK"""

    data: Instance
    r"""Detailed information about the instance."""
