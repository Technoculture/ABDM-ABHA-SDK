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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from abdm_gateway.models.consent_manager_patient_id import ConsentManagerPatientID
from abdm_gateway.models.hiu_subscription_context import HIUSubscriptionContext
from abdm_gateway.models.organization_representation import OrganizationRepresentation
from typing import Optional, Set
from typing_extensions import Self

class HIUSubscription(BaseModel):
    """
    HIUSubscription
    """ # noqa: E501
    id: StrictStr
    patient: ConsentManagerPatientID
    hiu: OrganizationRepresentation
    sources: List[HIUSubscriptionContext]
    __properties: ClassVar[List[str]] = ["id", "patient", "hiu", "sources"]

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
        """Create an instance of HIUSubscription from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of hiu
        if self.hiu:
            _dict['hiu'] = self.hiu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HIUSubscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "patient": ConsentManagerPatientID.from_dict(obj["patient"]) if obj.get("patient") is not None else None,
            "hiu": OrganizationRepresentation.from_dict(obj["hiu"]) if obj.get("hiu") is not None else None,
            "sources": [HIUSubscriptionContext.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None
        })
        return _obj


