"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .publicregioncode import PublicRegionCode
from lambda_cloud_sdk.types import BaseModel
from typing_extensions import TypedDict


class RegionTypedDict(TypedDict):
    name: PublicRegionCode
    description: str
    r"""The location represented by the region code."""


class Region(BaseModel):
    name: PublicRegionCode

    description: str
    r"""The location represented by the region code."""
