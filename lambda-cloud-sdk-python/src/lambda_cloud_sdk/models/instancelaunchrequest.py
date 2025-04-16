"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .imagespecificationfamily import (
    ImageSpecificationFamily,
    ImageSpecificationFamilyTypedDict,
)
from .imagespecificationid import ImageSpecificationID, ImageSpecificationIDTypedDict
from .publicregioncode import PublicRegionCode
from lambda_cloud_sdk.types import BaseModel
from typing import List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


InstanceLaunchRequestImageTypedDict = TypeAliasType(
    "InstanceLaunchRequestImageTypedDict",
    Union[ImageSpecificationIDTypedDict, ImageSpecificationFamilyTypedDict],
)
r"""The machine image you want to use. Defaults to the latest Lambda Stack image."""


InstanceLaunchRequestImage = TypeAliasType(
    "InstanceLaunchRequestImage", Union[ImageSpecificationID, ImageSpecificationFamily]
)
r"""The machine image you want to use. Defaults to the latest Lambda Stack image."""


class InstanceLaunchRequestTypedDict(TypedDict):
    region_name: PublicRegionCode
    instance_type_name: str
    r"""The type of instance you want to launch. To retrieve a list of available instance types, see
    [List available instance types](#get-/api/v1/instance-types).
    """
    ssh_key_names: List[str]
    r"""The names of the SSH keys you want to use to provide access to the instance.
    Currently, exactly one SSH key must be specified.
    """
    file_system_names: NotRequired[List[str]]
    r"""The names of the filesystems you want to attach to the instance.
    Currently, you can attach only one filesystem during instance creation.
    By default, no filesystems are attached.
    """
    name: NotRequired[str]
    r"""The name you want to assign to your instance. Must be 64 characters or fewer."""
    image: NotRequired[InstanceLaunchRequestImageTypedDict]
    r"""The machine image you want to use. Defaults to the latest Lambda Stack image."""
    user_data: NotRequired[str]
    r"""An instance configuration string specified in a valid
    [cloud-init user-data](https://cloudinit.readthedocs.io/en/latest/explanation/format.html)
    format. You can use this field to configure your instance on launch. The
    user data string must be plain text and cannot exceed 1MB in size.
    """


class InstanceLaunchRequest(BaseModel):
    region_name: PublicRegionCode

    instance_type_name: str
    r"""The type of instance you want to launch. To retrieve a list of available instance types, see
    [List available instance types](#get-/api/v1/instance-types).
    """

    ssh_key_names: List[str]
    r"""The names of the SSH keys you want to use to provide access to the instance.
    Currently, exactly one SSH key must be specified.
    """

    file_system_names: Optional[List[str]] = None
    r"""The names of the filesystems you want to attach to the instance.
    Currently, you can attach only one filesystem during instance creation.
    By default, no filesystems are attached.
    """

    name: Optional[str] = None
    r"""The name you want to assign to your instance. Must be 64 characters or fewer."""

    image: Optional[InstanceLaunchRequestImage] = None
    r"""The machine image you want to use. Defaults to the latest Lambda Stack image."""

    user_data: Optional[str] = None
    r"""An instance configuration string specified in a valid
    [cloud-init user-data](https://cloudinit.readthedocs.io/en/latest/explanation/format.html)
    format. You can use this field to configure your instance on launch. The
    user data string must be plain text and cannot exceed 1MB in size.
    """
