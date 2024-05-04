# PatientDiscoveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request. | 
**timestamp** | **datetime** | Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ | 
**transaction_id** | **str** | correlation-Id for patient discovery and subsequent care context linkage | 
**patient** | [**PatientDiscoveryRequestPatient**](PatientDiscoveryRequestPatient.md) |  | 

## Example

```python
from abdm_gateway.models.patient_discovery_request import PatientDiscoveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatientDiscoveryRequest from a JSON string
patient_discovery_request_instance = PatientDiscoveryRequest.from_json(json)
# print the JSON string representation of the object
print(PatientDiscoveryRequest.to_json())

# convert the object into a dict
patient_discovery_request_dict = patient_discovery_request_instance.to_dict()
# create an instance of PatientDiscoveryRequest from a dict
patient_discovery_request_from_dict = PatientDiscoveryRequest.from_dict(patient_discovery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


