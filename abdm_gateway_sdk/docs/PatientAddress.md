# PatientAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**pincode** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.patient_address import PatientAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PatientAddress from a JSON string
patient_address_instance = PatientAddress.from_json(json)
# print the JSON string representation of the object
print(PatientAddress.to_json())

# convert the object into a dict
patient_address_dict = patient_address_instance.to_dict()
# create an instance of PatientAddress from a dict
patient_address_from_dict = PatientAddress.from_dict(patient_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


