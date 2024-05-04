# CreateHidBiometricRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadhaar** | **str** |  | 
**auto_generated_benefit_id** | **bool** |  | [optional] 
**benefit_id** | **str** |  | [optional] 
**benefit_name** | **str** |  | 
**bio_type** | **str** |  | [optional] 
**consent_health_id** | **bool** |  | [optional] 
**mobile_number** | **str** |  | [optional] 
**pid** | **str** |  | 
**validity** | **str** |  | [optional] 

## Example

```python
from abha.models.create_hid_biometric_request import CreateHidBiometricRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHidBiometricRequest from a JSON string
create_hid_biometric_request_instance = CreateHidBiometricRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHidBiometricRequest.to_json())

# convert the object into a dict
create_hid_biometric_request_dict = create_hid_biometric_request_instance.to_dict()
# create an instance of CreateHidBiometricRequest from a dict
create_hid_biometric_request_from_dict = CreateHidBiometricRequest.from_dict(create_hid_biometric_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


