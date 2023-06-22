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
class AwsXrayResourcepolicy(BaseModel):
    PolicyName: Optional[str]
    PolicyDocument: Optional[str]
    BypassPolicyLockoutCheck: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AwsXrayResourcepolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsXrayResourcepolicy"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            PolicyName=json_data.get("PolicyName"),
            PolicyDocument=json_data.get("PolicyDocument"),
            BypassPolicyLockoutCheck=json_data.get("BypassPolicyLockoutCheck"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsXrayResourcepolicy = AwsXrayResourcepolicy


