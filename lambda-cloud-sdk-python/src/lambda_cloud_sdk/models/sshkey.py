"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from lambda_cloud_sdk.types import BaseModel
from typing_extensions import TypedDict


class SSHKeyTypedDict(TypedDict):
    r"""Information about a stored SSH key, which can be used to access instances over
    SSH.
    """

    id: str
    r"""The unique identifier (ID) of the SSH key."""
    name: str
    r"""The name of the SSH key."""
    public_key: str
    r"""The public key for the SSH key."""


class SSHKey(BaseModel):
    r"""Information about a stored SSH key, which can be used to access instances over
    SSH.
    """

    id: str
    r"""The unique identifier (ID) of the SSH key."""

    name: str
    r"""The name of the SSH key."""

    public_key: str
    r"""The public key for the SSH key."""
