# AadharNumberWebOptionalRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadhaar** | **str** | Encrypted with public key | [optional] 

## Example

```python
from abha.models.aadhar_number_web_optional_request_payload import AadharNumberWebOptionalRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AadharNumberWebOptionalRequestPayload from a JSON string
aadhar_number_web_optional_request_payload_instance = AadharNumberWebOptionalRequestPayload.from_json(json)
# print the JSON string representation of the object
print(AadharNumberWebOptionalRequestPayload.to_json())

# convert the object into a dict
aadhar_number_web_optional_request_payload_dict = aadhar_number_web_optional_request_payload_instance.to_dict()
# create an instance of AadharNumberWebOptionalRequestPayload from a dict
aadhar_number_web_optional_request_payload_from_dict = AadharNumberWebOptionalRequestPayload.from_dict(aadhar_number_web_optional_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


