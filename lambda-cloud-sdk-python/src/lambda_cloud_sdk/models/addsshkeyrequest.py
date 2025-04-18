"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from lambda_cloud_sdk.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AddSSHKeyRequestTypedDict(TypedDict):
    name: str
    r"""The name of the SSH key."""
    public_key: NotRequired[str]
    r"""The public key for the SSH key."""


class AddSSHKeyRequest(BaseModel):
    name: str
    r"""The name of the SSH key."""

    public_key: Optional[str] = None
    r"""The public key for the SSH key."""
