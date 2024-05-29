# V10PatientsProfileSharePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | a nonce, unique for each HTTP request | 

## Example

```python
from abha.models.v10_patients_profile_share_post_request import V10PatientsProfileSharePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V10PatientsProfileSharePostRequest from a JSON string
v10_patients_profile_share_post_request_instance = V10PatientsProfileSharePostRequest.from_json(json)
# print the JSON string representation of the object
print(V10PatientsProfileSharePostRequest.to_json())

# convert the object into a dict
v10_patients_profile_share_post_request_dict = v10_patients_profile_share_post_request_instance.to_dict()
# create an instance of V10PatientsProfileSharePostRequest from a dict
v10_patients_profile_share_post_request_from_dict = V10PatientsProfileSharePostRequest.from_dict(v10_patients_profile_share_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


