# coding: utf-8

"""
    Abdm Abha

    Abdm SDK for abha

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from abha.models.profile_share2_request_one_of_response import ProfileShare2RequestOneOfResponse
from typing import Optional, Set
from typing_extensions import Self

class LinkToken1RequestOneOf(BaseModel):
    """
    LinkToken1RequestOneOf
    """ # noqa: E501
    abha_address: Optional[StrictStr] = Field(default=None, alias="abhaAddress")
    link_token: Optional[StrictStr] = Field(alias="linkToken")
    response: ProfileShare2RequestOneOfResponse
    __properties: ClassVar[List[str]] = ["abhaAddress", "linkToken", "response"]

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
        """Create an instance of LinkToken1RequestOneOf from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of response
        if self.response:
            _dict['response'] = self.response.to_dict()
        # set to None if link_token (nullable) is None
        # and model_fields_set contains the field
        if self.link_token is None and "link_token" in self.model_fields_set:
            _dict['linkToken'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LinkToken1RequestOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abhaAddress": obj.get("abhaAddress"),
            "linkToken": obj.get("linkToken"),
            "response": ProfileShare2RequestOneOfResponse.from_dict(obj["response"]) if obj.get("response") is not None else None
        })
        return _obj


