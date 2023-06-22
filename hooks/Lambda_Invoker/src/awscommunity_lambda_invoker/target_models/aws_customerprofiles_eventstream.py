# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsCustomerprofilesEventstream(BaseModel):
    DomainName: Optional[str]
    EventStreamName: Optional[str]
    Uri: Optional[str]
    EventStreamArn: Optional[str]
    Tags: Optional[Any]
    CreatedAt: Optional[str]
    State: Optional[str]
    DestinationDetails: Optional["_DestinationDetails"]

    @classmethod
    def _deserialize(
        cls: Type["_AwsCustomerprofilesEventstream"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsCustomerprofilesEventstream"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            DomainName=json_data.get("DomainName"),
            EventStreamName=json_data.get("EventStreamName"),
            Uri=json_data.get("Uri"),
            EventStreamArn=json_data.get("EventStreamArn"),
            Tags=json_data.get("Tags"),
            CreatedAt=json_data.get("CreatedAt"),
            State=json_data.get("State"),
            DestinationDetails=DestinationDetails._deserialize(json_data.get("DestinationDetails")),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsCustomerprofilesEventstream = AwsCustomerprofilesEventstream


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


@dataclass
class DestinationDetails(BaseModel):
    Uri: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDetails"]:
        if not json_data:
            return None
        return cls(
            Uri=json_data.get("Uri"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDetails = DestinationDetails


