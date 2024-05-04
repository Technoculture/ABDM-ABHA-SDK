# ConsentRequestInitResponseConsentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the consent-request created | 

## Example

```python
from abdm_gateway.models.consent_request_init_response_consent_request import ConsentRequestInitResponseConsentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestInitResponseConsentRequest from a JSON string
consent_request_init_response_consent_request_instance = ConsentRequestInitResponseConsentRequest.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestInitResponseConsentRequest.to_json())

# convert the object into a dict
consent_request_init_response_consent_request_dict = consent_request_init_response_consent_request_instance.to_dict()
# create an instance of ConsentRequestInitResponseConsentRequest from a dict
consent_request_init_response_consent_request_from_dict = ConsentRequestInitResponseConsentRequest.from_dict(consent_request_init_response_consent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


