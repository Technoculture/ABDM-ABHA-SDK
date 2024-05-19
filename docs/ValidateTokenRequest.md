# ValidateTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** |  | 

## Example

```python
from abha.models.validate_token_request import ValidateTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateTokenRequest from a JSON string
validate_token_request_instance = ValidateTokenRequest.from_json(json)
# print the JSON string representation of the object
print(ValidateTokenRequest.to_json())

# convert the object into a dict
validate_token_request_dict = validate_token_request_instance.to_dict()
# create an instance of ValidateTokenRequest from a dict
validate_token_request_from_dict = ValidateTokenRequest.from_dict(validate_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


