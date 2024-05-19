# coding: utf-8

"""
    ABHA Service

    It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue an ABHA Number to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.  The ABHA Number will be used for the purposes of uniquely identifying persons and authenticating them. An ABHA Address will be used for threading their health records (only with the informed consent of the patient) across multiple systems and stakeholders.   <b>API Security</b>  You need Authorization Token and X-HIP-ID to consume APIs. <b>Notes:</b>  <b>1. In case you want to consume the ABHA APIs and use creation on your own interface, use authentication methods as OTP only. </b> <b>2. In order to have access to ABHA APIs, your clientId must have hid role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request.</b> <b>3. In order to have access to Integrated Programs ABHA APIs, your clientId must have integrated_program role in gateway. So if you want access to these APIs then please request it in your ABDM on-boarding request. Also you will need to share integrated program benefit name to be used in this case.</b> <b>4. When calling APIs, please ensure that Authorization header must have format as <i>Bearer {Token_Value}</i>. Please note that prefix Bearer is followed by space before the token value.</b> <b>5. Check the state and district codes from LGD directory [click here](https://lgdirectory.gov.in/)</b>  <b>6. For the APIs </b>  - Sensitive data (Data like OTP, Aadhaar Number, Password, Username etc) have to be encrypted. - Data is encrypted by the public certificate. The certificate can be downloaded from the __/v1/auth/cert__ API under __Authentication__ tag. - RSA Encryption to encrypt the data. Cipher Type - <b>RSA/ECB/PKCS1Padding</b>.  online tool to encrypt data [click here](https://www.devglan.com/online-tools/rsa-encryption-decryption)  <b>

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class File(BaseModel):
    """
    File
    """ # noqa: E501
    absolute: Optional[StrictBool] = None
    absolute_file: Optional[File] = Field(default=None, alias="absoluteFile")
    absolute_path: Optional[StrictStr] = Field(default=None, alias="absolutePath")
    canonical_file: Optional[File] = Field(default=None, alias="canonicalFile")
    canonical_path: Optional[StrictStr] = Field(default=None, alias="canonicalPath")
    directory: Optional[StrictBool] = None
    file: Optional[StrictBool] = None
    free_space: Optional[StrictInt] = Field(default=None, alias="freeSpace")
    hidden: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    parent: Optional[StrictStr] = None
    parent_file: Optional[File] = Field(default=None, alias="parentFile")
    path: Optional[StrictStr] = None
    total_space: Optional[StrictInt] = Field(default=None, alias="totalSpace")
    usable_space: Optional[StrictInt] = Field(default=None, alias="usableSpace")
    __properties: ClassVar[List[str]] = ["absolute", "absoluteFile", "absolutePath", "canonicalFile", "canonicalPath", "directory", "file", "freeSpace", "hidden", "name", "parent", "parentFile", "path", "totalSpace", "usableSpace"]

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
        """Create an instance of File from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of absolute_file
        if self.absolute_file:
            _dict['absoluteFile'] = self.absolute_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of canonical_file
        if self.canonical_file:
            _dict['canonicalFile'] = self.canonical_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_file
        if self.parent_file:
            _dict['parentFile'] = self.parent_file.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of File from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "absolute": obj.get("absolute"),
            "absoluteFile": File.from_dict(obj["absoluteFile"]) if obj.get("absoluteFile") is not None else None,
            "absolutePath": obj.get("absolutePath"),
            "canonicalFile": File.from_dict(obj["canonicalFile"]) if obj.get("canonicalFile") is not None else None,
            "canonicalPath": obj.get("canonicalPath"),
            "directory": obj.get("directory"),
            "file": obj.get("file"),
            "freeSpace": obj.get("freeSpace"),
            "hidden": obj.get("hidden"),
            "name": obj.get("name"),
            "parent": obj.get("parent"),
            "parentFile": File.from_dict(obj["parentFile"]) if obj.get("parentFile") is not None else None,
            "path": obj.get("path"),
            "totalSpace": obj.get("totalSpace"),
            "usableSpace": obj.get("usableSpace")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
File.model_rebuild(raise_errors=False)

