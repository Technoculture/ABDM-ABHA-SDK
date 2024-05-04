# FacilityFaceAuthSessionWaitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devip** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from abha.models.facility_face_auth_session_wait_response import FacilityFaceAuthSessionWaitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityFaceAuthSessionWaitResponse from a JSON string
facility_face_auth_session_wait_response_instance = FacilityFaceAuthSessionWaitResponse.from_json(json)
# print the JSON string representation of the object
print(FacilityFaceAuthSessionWaitResponse.to_json())

# convert the object into a dict
facility_face_auth_session_wait_response_dict = facility_face_auth_session_wait_response_instance.to_dict()
# create an instance of FacilityFaceAuthSessionWaitResponse from a dict
facility_face_auth_session_wait_response_from_dict = FacilityFaceAuthSessionWaitResponse.from_dict(facility_face_auth_session_wait_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


