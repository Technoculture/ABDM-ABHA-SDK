# AadharNumberRequestPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadhaar** | **str** |  | [optional] 

## Example

```python
from abha.models.aadhar_number_request_payload import AadharNumberRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AadharNumberRequestPayload from a JSON string
aadhar_number_request_payload_instance = AadharNumberRequestPayload.from_json(json)
# print the JSON string representation of the object
print(AadharNumberRequestPayload.to_json())

# convert the object into a dict
aadhar_number_request_payload_dict = aadhar_number_request_payload_instance.to_dict()
# create an instance of AadharNumberRequestPayload from a dict
aadhar_number_request_payload_from_dict = AadharNumberRequestPayload.from_dict(aadhar_number_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


