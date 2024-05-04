# GenerateMobileOTPRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile** | **str** |  | 

## Example

```python
from abha.models.generate_mobile_otp_request import GenerateMobileOTPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateMobileOTPRequest from a JSON string
generate_mobile_otp_request_instance = GenerateMobileOTPRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateMobileOTPRequest.to_json())

# convert the object into a dict
generate_mobile_otp_request_dict = generate_mobile_otp_request_instance.to_dict()
# create an instance of GenerateMobileOTPRequest from a dict
generate_mobile_otp_request_from_dict = GenerateMobileOTPRequest.from_dict(generate_mobile_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


