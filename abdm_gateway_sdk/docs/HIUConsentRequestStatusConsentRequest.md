# HIUConsentRequestStatusConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**status** | [**ConsentStatus**](ConsentStatus.md) |  | 
**consent_artefacts** | [**List[ConsentArtefactReference]**](ConsentArtefactReference.md) |  | [optional] 

## Example

```python
from abdm_gateway.models.hiu_consent_request_status_consent_request import HIUConsentRequestStatusConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HIUConsentRequestStatusConsentRequest from a JSON string
hiu_consent_request_status_consent_request_instance = HIUConsentRequestStatusConsentRequest.from_json(json)
# print the JSON string representation of the object
print(HIUConsentRequestStatusConsentRequest.to_json())

# convert the object into a dict
hiu_consent_request_status_consent_request_dict = hiu_consent_request_status_consent_request_instance.to_dict()
# create an instance of HIUConsentRequestStatusConsentRequest from a dict
hiu_consent_request_status_consent_request_from_dict = HIUConsentRequestStatusConsentRequest.from_dict(hiu_consent_request_status_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


