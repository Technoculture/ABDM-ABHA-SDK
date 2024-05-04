# FacilityFaceAuthSessionInitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qrcode** | **str** |  | [optional] 
**suid** | **str** |  | [optional] 

## Example

```python
from abha.models.facility_face_auth_session_init_response import FacilityFaceAuthSessionInitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityFaceAuthSessionInitResponse from a JSON string
facility_face_auth_session_init_response_instance = FacilityFaceAuthSessionInitResponse.from_json(json)
# print the JSON string representation of the object
print(FacilityFaceAuthSessionInitResponse.to_json())

# convert the object into a dict
facility_face_auth_session_init_response_dict = facility_face_auth_session_init_response_instance.to_dict()
# create an instance of FacilityFaceAuthSessionInitResponse from a dict
facility_face_auth_session_init_response_from_dict = FacilityFaceAuthSessionInitResponse.from_dict(facility_face_auth_session_init_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


