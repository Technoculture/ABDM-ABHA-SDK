# ByteArrayResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**byte_array** | **bytearray** |  | [optional] 
**description** | **str** |  | [optional] 
**file** | [**File**](File.md) |  | [optional] 
**filename** | **str** |  | [optional] 
**input_stream** | **object** |  | [optional] 
**open** | **bool** |  | [optional] 
**readable** | **bool** |  | [optional] 
**uri** | **str** |  | [optional] 
**url** | [**URL**](URL.md) |  | [optional] 

## Example

```python
from abha.models.byte_array_resource import ByteArrayResource

# TODO update the JSON string below
json = "{}"
# create an instance of ByteArrayResource from a JSON string
byte_array_resource_instance = ByteArrayResource.from_json(json)
# print the JSON string representation of the object
print(ByteArrayResource.to_json())

# convert the object into a dict
byte_array_resource_dict = byte_array_resource_instance.to_dict()
# create an instance of ByteArrayResource from a dict
byte_array_resource_from_dict = ByteArrayResource.from_dict(byte_array_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


