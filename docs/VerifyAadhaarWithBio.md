# VerifyAadhaarWithBio


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadhaar** | **str** |  | 
**bio_type** | **str** |  | [optional] 
**pid** | **str** |  | 

## Example

```python
from abha.models.verify_aadhaar_with_bio import VerifyAadhaarWithBio

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAadhaarWithBio from a JSON string
verify_aadhaar_with_bio_instance = VerifyAadhaarWithBio.from_json(json)
# print the JSON string representation of the object
print(VerifyAadhaarWithBio.to_json())

# convert the object into a dict
verify_aadhaar_with_bio_dict = verify_aadhaar_with_bio_instance.to_dict()
# create an instance of VerifyAadhaarWithBio from a dict
verify_aadhaar_with_bio_from_dict = VerifyAadhaarWithBio.from_dict(verify_aadhaar_with_bio_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


