"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from lambda_cloud_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class InstanceModificationRequestTypedDict(TypedDict):
    name: NotRequired[str]
    r"""The new, user-provided name for the instance."""


class InstanceModificationRequest(BaseModel):
    name: Optional[str] = None
    r"""The new, user-provided name for the instance."""
