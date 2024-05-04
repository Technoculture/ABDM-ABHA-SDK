# coding: utf-8

"""
    Gateway

    Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from abdm_gateway.models.permission_date_range import PermissionDateRange
from abdm_gateway.models.permission_frequency import PermissionFrequency
from typing import Optional, Set
from typing_extensions import Self

class Permission(BaseModel):
    """
    Permission
    """ # noqa: E501
    access_mode: StrictStr = Field(alias="accessMode")
    date_range: PermissionDateRange = Field(alias="dateRange")
    data_erase_at: datetime = Field(alias="dataEraseAt")
    frequency: PermissionFrequency
    __properties: ClassVar[List[str]] = ["accessMode", "dateRange", "dataEraseAt", "frequency"]

    @field_validator('access_mode')
    def access_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['VIEW', 'STORE', 'QUERY', 'STREAM']):
            raise ValueError("must be one of enum values ('VIEW', 'STORE', 'QUERY', 'STREAM')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Permission from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of date_range
        if self.date_range:
            _dict['dateRange'] = self.date_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of frequency
        if self.frequency:
            _dict['frequency'] = self.frequency.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Permission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessMode": obj.get("accessMode"),
            "dateRange": PermissionDateRange.from_dict(obj["dateRange"]) if obj.get("dateRange") is not None else None,
            "dataEraseAt": obj.get("dataEraseAt"),
            "frequency": PermissionFrequency.from_dict(obj["frequency"]) if obj.get("frequency") is not None else None
        })
        return _obj


