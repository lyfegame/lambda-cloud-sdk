"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from lambda_cloud_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class APIErrorInvalidParametersTypedDict(TypedDict):
    code: NotRequired[str]
    r"""The unique identifier for the type of error."""
    message: NotRequired[str]
    r"""A description of the error."""
    suggestion: NotRequired[str]
    r"""One or more suggestions of possible ways to fix the error."""


class APIErrorInvalidParameters(BaseModel):
    code: Optional[str] = "global/invalid-parameters"
    r"""The unique identifier for the type of error."""

    message: Optional[str] = "Invalid request data."
    r"""A description of the error."""

    suggestion: Optional[str] = None
    r"""One or more suggestions of possible ways to fix the error."""
