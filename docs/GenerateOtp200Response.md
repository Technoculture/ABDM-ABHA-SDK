# GenerateOtp200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txn_id** | **str** | Based on UUID | [optional] 

## Example

```python
from abha.models.generate_otp200_response import GenerateOtp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateOtp200Response from a JSON string
generate_otp200_response_instance = GenerateOtp200Response.from_json(json)
# print the JSON string representation of the object
print(GenerateOtp200Response.to_json())

# convert the object into a dict
generate_otp200_response_dict = generate_otp200_response_instance.to_dict()
# create an instance of GenerateOtp200Response from a dict
generate_otp200_response_from_dict = GenerateOtp200Response.from_dict(generate_otp200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


