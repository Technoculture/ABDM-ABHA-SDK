# GenerateOtpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aadhaar** | **str** | The Aadhaar number for which to generate the OTP. | [optional] 

## Example

```python
from abha.models.generate_otp_request import GenerateOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateOtpRequest from a JSON string
generate_otp_request_instance = GenerateOtpRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateOtpRequest.to_json())

# convert the object into a dict
generate_otp_request_dict = generate_otp_request_instance.to_dict()
# create an instance of GenerateOtpRequest from a dict
generate_otp_request_from_dict = GenerateOtpRequest.from_dict(generate_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


