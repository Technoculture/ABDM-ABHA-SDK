# EventCategoryDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**care_context** | [**CareContextDefinition**](CareContextDefinition.md) |  | 
**hi_types** | [**List[HITypeEnum]**](HITypeEnum.md) |  | 

## Example

```python
from abdm_gateway.models.event_category_detail import EventCategoryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EventCategoryDetail from a JSON string
event_category_detail_instance = EventCategoryDetail.from_json(json)
# print the JSON string representation of the object
print(EventCategoryDetail.to_json())

# convert the object into a dict
event_category_detail_dict = event_category_detail_instance.to_dict()
# create an instance of EventCategoryDetail from a dict
event_category_detail_from_dict = EventCategoryDetail.from_dict(event_category_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


