"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .apierroraccountinactive import APIErrorAccountInactive
from .apierrorinstancenotfound import APIErrorInstanceNotFound
from .apierrorunauthorized import APIErrorUnauthorized
from .instancerestartresponse import (
    InstanceRestartResponse,
    InstanceRestartResponseTypedDict,
)
from .schemebasicauth import SchemeBasicAuth, SchemeBasicAuthTypedDict
from lambda_cloud_sdk import utils
from lambda_cloud_sdk.types import BaseModel
from lambda_cloud_sdk.utils import FieldMetadata, SecurityMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class RestartInstanceSecurityTypedDict(TypedDict):
    basic_auth: NotRequired[SchemeBasicAuthTypedDict]
    bearer_auth: NotRequired[str]


class RestartInstanceSecurity(BaseModel):
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


class RestartInstanceInstancesResponse404ResponseBodyData(BaseModel):
    error: APIErrorInstanceNotFound


class RestartInstanceInstancesResponse404ResponseBody(Exception):
    r"""Not Found"""

    data: RestartInstanceInstancesResponse404ResponseBodyData

    def __init__(self, data: RestartInstanceInstancesResponse404ResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, RestartInstanceInstancesResponse404ResponseBodyData
        )


class RestartInstanceInstancesResponseResponseBodyData(BaseModel):
    error: APIErrorAccountInactive


class RestartInstanceInstancesResponseResponseBody(Exception):
    r"""Forbidden"""

    data: RestartInstanceInstancesResponseResponseBodyData

    def __init__(self, data: RestartInstanceInstancesResponseResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(
            self.data, RestartInstanceInstancesResponseResponseBodyData
        )


class RestartInstanceInstancesResponseBodyData(BaseModel):
    error: APIErrorUnauthorized


class RestartInstanceInstancesResponseBody(Exception):
    r"""Unauthorized"""

    data: RestartInstanceInstancesResponseBodyData

    def __init__(self, data: RestartInstanceInstancesResponseBodyData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, RestartInstanceInstancesResponseBodyData)


class RestartInstanceResponseBodyTypedDict(TypedDict):
    r"""OK"""

    data: InstanceRestartResponseTypedDict


class RestartInstanceResponseBody(BaseModel):
    r"""OK"""

    data: InstanceRestartResponse
