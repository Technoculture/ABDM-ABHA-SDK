# ConsentRequestConsentPatient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 

## Example

```python
from abdm_gateway.models.consent_request_consent_patient import ConsentRequestConsentPatient

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentRequestConsentPatient from a JSON string
consent_request_consent_patient_instance = ConsentRequestConsentPatient.from_json(json)
# print the JSON string representation of the object
print(ConsentRequestConsentPatient.to_json())

# convert the object into a dict
consent_request_consent_patient_dict = consent_request_consent_patient_instance.to_dict()
# create an instance of ConsentRequestConsentPatient from a dict
consent_request_consent_patient_from_dict = ConsentRequestConsentPatient.from_dict(consent_request_consent_patient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


