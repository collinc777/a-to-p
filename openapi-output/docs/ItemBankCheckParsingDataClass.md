# ItemBankCheckParsingDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**amount_text** | **str** |  | 
**bank_address** | **str** |  | 
**bank_name** | **str** |  | 
**var_date** | **str** |  | 
**memo** | **str** |  | 
**payer_address** | **str** |  | 
**payer_name** | **str** |  | 
**receiver_address** | **str** |  | 
**receiver_name** | **str** |  | 
**currency** | **str** |  | 
**micr** | [**MicrModel**](MicrModel.md) |  | 

## Example

```python
from openapi_client.models.item_bank_check_parsing_data_class import ItemBankCheckParsingDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBankCheckParsingDataClass from a JSON string
item_bank_check_parsing_data_class_instance = ItemBankCheckParsingDataClass.from_json(json)
# print the JSON string representation of the object
print(ItemBankCheckParsingDataClass.to_json())

# convert the object into a dict
item_bank_check_parsing_data_class_dict = item_bank_check_parsing_data_class_instance.to_dict()
# create an instance of ItemBankCheckParsingDataClass from a dict
item_bank_check_parsing_data_class_form_dict = item_bank_check_parsing_data_class.from_dict(item_bank_check_parsing_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


