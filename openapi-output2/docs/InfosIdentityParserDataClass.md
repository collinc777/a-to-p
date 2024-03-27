# InfosIdentityParserDataClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_name** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**given_names** | [**List[ItemIdentityParserDataClass]**](ItemIdentityParserDataClass.md) |  | [optional] 
**birth_place** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**birth_date** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**issuance_date** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**expire_date** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**document_id** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**issuing_state** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**address** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**age** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**country** | [**Country**](Country.md) |  | 
**document_type** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**gender** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**image_id** | [**List[ItemIdentityParserDataClass]**](ItemIdentityParserDataClass.md) |  | [optional] 
**image_signature** | [**List[ItemIdentityParserDataClass]**](ItemIdentityParserDataClass.md) |  | [optional] 
**mrz** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 
**nationality** | [**ItemIdentityParserDataClass**](ItemIdentityParserDataClass.md) |  | 

## Example

```python
from openapi_client.models.infos_identity_parser_data_class import InfosIdentityParserDataClass

# TODO update the JSON string below
json = "{}"
# create an instance of InfosIdentityParserDataClass from a JSON string
infos_identity_parser_data_class_instance = InfosIdentityParserDataClass.from_json(json)
# print the JSON string representation of the object
print(InfosIdentityParserDataClass.to_json())

# convert the object into a dict
infos_identity_parser_data_class_dict = infos_identity_parser_data_class_instance.to_dict()
# create an instance of InfosIdentityParserDataClass from a dict
infos_identity_parser_data_class_form_dict = infos_identity_parser_data_class.from_dict(infos_identity_parser_data_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


