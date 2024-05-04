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
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from abdm_gateway.models.care_context_definition import CareContextDefinition
from abdm_gateway.models.hi_type_enum import HITypeEnum
from abdm_gateway.models.hip_data_notification_request_notification_hip import HipDataNotificationRequestNotificationHip
from abdm_gateway.models.hip_data_notification_request_notification_patient import HipDataNotificationRequestNotificationPatient
from typing import Optional, Set
from typing_extensions import Self

class HipDataNotificationRequestNotification(BaseModel):
    """
    HipDataNotificationRequestNotification
    """ # noqa: E501
    patient: HipDataNotificationRequestNotificationPatient
    care_context: CareContextDefinition = Field(alias="careContext")
    hi_types: List[HITypeEnum] = Field(description="Type of health data that created in the care context", alias="hiTypes")
    var_date: datetime = Field(description="Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ", alias="date")
    hip: HipDataNotificationRequestNotificationHip
    __properties: ClassVar[List[str]] = ["patient", "careContext", "hiTypes", "date", "hip"]

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
        """Create an instance of HipDataNotificationRequestNotification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of patient
        if self.patient:
            _dict['patient'] = self.patient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of care_context
        if self.care_context:
            _dict['careContext'] = self.care_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hip
        if self.hip:
            _dict['hip'] = self.hip.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HipDataNotificationRequestNotification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "patient": HipDataNotificationRequestNotificationPatient.from_dict(obj["patient"]) if obj.get("patient") is not None else None,
            "careContext": CareContextDefinition.from_dict(obj["careContext"]) if obj.get("careContext") is not None else None,
            "hiTypes": obj.get("hiTypes"),
            "date": obj.get("date"),
            "hip": HipDataNotificationRequestNotificationHip.from_dict(obj["hip"]) if obj.get("hip") is not None else None
        })
        return _obj


