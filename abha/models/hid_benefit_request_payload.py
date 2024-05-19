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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from abha.models.jwt_response import JwtResponse
from typing import Optional, Set
from typing_extensions import Self

class HidBenefitRequestPayload(BaseModel):
    """
    HidBenefitRequestPayload
    """ # noqa: E501
    address: Optional[StrictStr] = None
    auth_methods: Optional[List[StrictStr]] = Field(default=None, description="Based on authMethods", alias="authMethods")
    benefit_id: Optional[StrictStr] = Field(default=None, alias="benefitId")
    day_of_birth: Optional[StrictStr] = Field(default=None, alias="dayOfBirth")
    district_code: Optional[StrictStr] = Field(default=None, alias="districtCode")
    district_name: Optional[StrictStr] = Field(default=None, alias="districtName")
    email: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    gender: Optional[StrictStr] = None
    health_id: Optional[StrictStr] = Field(default=None, alias="healthId")
    health_id_number: Optional[StrictStr] = Field(default=None, alias="healthIdNumber")
    kyc_photo: Optional[StrictStr] = Field(default=None, description="Encoded with Base 64", alias="kycPhoto")
    kyc_verified: Optional[StrictBool] = Field(default=None, alias="kycVerified")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    middle_name: Optional[StrictStr] = Field(default=None, alias="middleName")
    mobile: Optional[StrictStr] = None
    month_of_birth: Optional[StrictStr] = Field(default=None, alias="monthOfBirth")
    name: Optional[StrictStr] = None
    new: Optional[StrictBool] = None
    pincode: Optional[StrictStr] = None
    profile_photo: Optional[StrictStr] = Field(default=None, description="Encoded with Base 64", alias="profilePhoto")
    state_code: Optional[StrictStr] = Field(default=None, alias="stateCode")
    state_name: Optional[StrictStr] = Field(default=None, alias="stateName")
    status: Optional[StrictStr] = None
    sub_district_code: Optional[StrictStr] = Field(default=None, alias="subDistrictCode")
    subdistrict_name: Optional[StrictStr] = Field(default=None, alias="subdistrictName")
    tags: Optional[Dict[str, StrictStr]] = None
    token: Optional[JwtResponse] = None
    town_code: Optional[StrictStr] = Field(default=None, alias="townCode")
    town_name: Optional[StrictStr] = Field(default=None, alias="townName")
    village_code: Optional[StrictStr] = Field(default=None, alias="villageCode")
    village_name: Optional[StrictStr] = Field(default=None, alias="villageName")
    ward_code: Optional[StrictStr] = Field(default=None, alias="wardCode")
    ward_name: Optional[StrictStr] = Field(default=None, alias="wardName")
    year_of_birth: Optional[StrictStr] = Field(default=None, alias="yearOfBirth")
    __properties: ClassVar[List[str]] = ["address", "authMethods", "benefitId", "dayOfBirth", "districtCode", "districtName", "email", "firstName", "gender", "healthId", "healthIdNumber", "kycPhoto", "kycVerified", "lastName", "middleName", "mobile", "monthOfBirth", "name", "new", "pincode", "profilePhoto", "stateCode", "stateName", "status", "subDistrictCode", "subdistrictName", "tags", "token", "townCode", "townName", "villageCode", "villageName", "wardCode", "wardName", "yearOfBirth"]

    @field_validator('auth_methods')
    def auth_methods_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['AADHAAR_OTP', 'MOBILE_OTP', 'PASSWORD', 'DEMOGRAPHICS', 'AADHAAR_BIO']):
                raise ValueError("each list item must be one of ('AADHAAR_OTP', 'MOBILE_OTP', 'PASSWORD', 'DEMOGRAPHICS', 'AADHAAR_BIO')")
        return value

    @field_validator('gender')
    def gender_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['M', 'F', 'T']):
            raise ValueError("must be one of enum values ('M', 'F', 'T')")
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
        """Create an instance of HidBenefitRequestPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HidBenefitRequestPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "authMethods": obj.get("authMethods"),
            "benefitId": obj.get("benefitId"),
            "dayOfBirth": obj.get("dayOfBirth"),
            "districtCode": obj.get("districtCode"),
            "districtName": obj.get("districtName"),
            "email": obj.get("email"),
            "firstName": obj.get("firstName"),
            "gender": obj.get("gender"),
            "healthId": obj.get("healthId"),
            "healthIdNumber": obj.get("healthIdNumber"),
            "kycPhoto": obj.get("kycPhoto"),
            "kycVerified": obj.get("kycVerified"),
            "lastName": obj.get("lastName"),
            "middleName": obj.get("middleName"),
            "mobile": obj.get("mobile"),
            "monthOfBirth": obj.get("monthOfBirth"),
            "name": obj.get("name"),
            "new": obj.get("new"),
            "pincode": obj.get("pincode"),
            "profilePhoto": obj.get("profilePhoto"),
            "stateCode": obj.get("stateCode"),
            "stateName": obj.get("stateName"),
            "status": obj.get("status"),
            "subDistrictCode": obj.get("subDistrictCode"),
            "subdistrictName": obj.get("subdistrictName"),
            "tags": obj.get("tags"),
            "token": JwtResponse.from_dict(obj["token"]) if obj.get("token") is not None else None,
            "townCode": obj.get("townCode"),
            "townName": obj.get("townName"),
            "villageCode": obj.get("villageCode"),
            "villageName": obj.get("villageName"),
            "wardCode": obj.get("wardCode"),
            "wardName": obj.get("wardName"),
            "yearOfBirth": obj.get("yearOfBirth")
        })
        return _obj


