"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from lambda_cloud_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class APIErrorFilesystemInUseTypedDict(TypedDict):
    message: str
    r"""A description of the error."""
    code: NotRequired[str]
    r"""The unique identifier for the type of error."""
    suggestion: NotRequired[str]
    r"""One or more suggestions of possible ways to fix the error."""


class APIErrorFilesystemInUse(BaseModel):
    message: str
    r"""A description of the error."""

    code: Optional[str] = "filesystems/filesystem-in-use"
    r"""The unique identifier for the type of error."""

    suggestion: Optional[str] = None
    r"""One or more suggestions of possible ways to fix the error."""
