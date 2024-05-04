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
from typing import Any, ClassVar, Dict, List, Optional
from abdm_gateway.models.error import Error
from abdm_gateway.models.request_reference import RequestReference
from typing import Optional, Set
from typing_extensions import Self

class PatientSMSNotifcationResponse(BaseModel):
    """
    PatientSMSNotifcationResponse
    """ # noqa: E501
    request_id: StrictStr = Field(description="a nonce, unique for each HTTP request", alias="requestId")
    timestamp: datetime = Field(description="Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ")
    status: Optional[StrictStr] = None
    error: Optional[Error] = None
    resp: RequestReference
    __properties: ClassVar[List[str]] = ["requestId", "timestamp", "status", "error", "resp"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ACKNOWLEDGED', 'ERRORED']):
            raise ValueError("must be one of enum values ('ACKNOWLEDGED', 'ERRORED')")
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
        """Create an instance of PatientSMSNotifcationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resp
        if self.resp:
            _dict['resp'] = self.resp.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatientSMSNotifcationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requestId": obj.get("requestId"),
            "timestamp": obj.get("timestamp"),
            "status": obj.get("status"),
            "error": Error.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "resp": RequestReference.from_dict(obj["resp"]) if obj.get("resp") is not None else None
        })
        return _obj


