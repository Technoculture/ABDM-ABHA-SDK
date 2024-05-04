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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from abdm_gateway.models.identifier import Identifier
from abdm_gateway.models.patient_gender import PatientGender
from typing import Optional, Set
from typing_extensions import Self

class PatientDiscoveryRequestPatient(BaseModel):
    """
    PatientDiscoveryRequestPatient
    """ # noqa: E501
    id: StrictStr = Field(description="Identifier of patient at consent manager")
    verified_identifiers: List[Identifier] = Field(alias="verifiedIdentifiers")
    unverified_identifiers: Optional[List[Identifier]] = Field(default=None, alias="unverifiedIdentifiers")
    name: StrictStr
    gender: PatientGender
    year_of_birth: StrictInt = Field(alias="yearOfBirth")
    __properties: ClassVar[List[str]] = ["id", "verifiedIdentifiers", "unverifiedIdentifiers", "name", "gender", "yearOfBirth"]

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
        """Create an instance of PatientDiscoveryRequestPatient from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in verified_identifiers (list)
        _items = []
        if self.verified_identifiers:
            for _item in self.verified_identifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['verifiedIdentifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in unverified_identifiers (list)
        _items = []
        if self.unverified_identifiers:
            for _item in self.unverified_identifiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['unverifiedIdentifiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatientDiscoveryRequestPatient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "verifiedIdentifiers": [Identifier.from_dict(_item) for _item in obj["verifiedIdentifiers"]] if obj.get("verifiedIdentifiers") is not None else None,
            "unverifiedIdentifiers": [Identifier.from_dict(_item) for _item in obj["unverifiedIdentifiers"]] if obj.get("unverifiedIdentifiers") is not None else None,
            "name": obj.get("name"),
            "gender": obj.get("gender"),
            "yearOfBirth": obj.get("yearOfBirth")
        })
        return _obj

