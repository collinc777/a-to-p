# AnonymizationEntity

This model represents an entity extracted from the text.      Attributes:         offset (int): The offset of the entity in the text.         length (int): The lenght of the entity in the text.         category (CategoryType): The category of the entity.         subcategory (SubCategoryType): The subcategory of the entity.         original_label (str): The original label of the entity.         content (str): The content of the entity.     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**length** | **int** |  | 
**category** | [**CategoryType**](CategoryType.md) |  | 
**subcategory** | [**Subcategory**](Subcategory.md) |  | 
**original_label** | **str** |  | 
**content** | **str** |  | 
**confidence_score** | **int** |  | 

## Example

```python
from openapi_client.models.anonymization_entity import AnonymizationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AnonymizationEntity from a JSON string
anonymization_entity_instance = AnonymizationEntity.from_json(json)
# print the JSON string representation of the object
print(AnonymizationEntity.to_json())

# convert the object into a dict
anonymization_entity_dict = anonymization_entity_instance.to_dict()
# create an instance of AnonymizationEntity from a dict
anonymization_entity_form_dict = anonymization_entity.from_dict(anonymization_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


