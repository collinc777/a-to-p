# PersonAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upper_cloths** | [**List[UpperCloth]**](UpperCloth.md) |  | [optional] 
**lower_cloths** | [**List[LowerCloth]**](LowerCloth.md) |  | [optional] 

## Example

```python
from openapi_client.models.person_attributes import PersonAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of PersonAttributes from a JSON string
person_attributes_instance = PersonAttributes.from_json(json)
# print the JSON string representation of the object
print(PersonAttributes.to_json())

# convert the object into a dict
person_attributes_dict = person_attributes_instance.to_dict()
# create an instance of PersonAttributes from a dict
person_attributes_form_dict = person_attributes.from_dict(person_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


