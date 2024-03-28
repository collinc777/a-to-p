# FinancialLineItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax** | **int** | Tax amount for the line item. | [optional] 
**amount_line** | **int** | Total amount for the line item. | [optional] 
**description** | **str** | Description of the line item. | [optional] 
**quantity** | **int** | Quantity of units for the line item. | [optional] 
**unit_price** | **int** | Unit price for each unit in the line item. | [optional] 
**unit_type** | **str** | Type of unit (e.g., hours, items). | [optional] 
**var_date** | **str** | Date associated with the line item. | [optional] 
**product_code** | **str** | Product code or identifier for the line item. | [optional] 
**purchase_order** | **str** | Purchase order related to the line item. | [optional] 
**tax_rate** | **int** | Tax rate applied to the line item. | [optional] 
**base_total** | **int** | Base total amount before any discounts or taxes. | [optional] 
**sub_total** | **int** | Subtotal amount for the line item. | [optional] 
**discount_amount** | **int** | Amount of discount applied to the line item. | [optional] 
**discount_rate** | **int** | Rate of discount applied to the line item. | [optional] 
**discount_code** | **str** | Code associated with any discount applied to the line item. | [optional] 
**order_number** | **str** | Order number associated with the line item. | [optional] 
**title** | **str** | Title or name of the line item. | [optional] 

## Example

```python
from openapi_client.models.financial_line_item import FinancialLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialLineItem from a JSON string
financial_line_item_instance = FinancialLineItem.from_json(json)
# print the JSON string representation of the object
print(FinancialLineItem.to_json())

# convert the object into a dict
financial_line_item_dict = financial_line_item_instance.to_dict()
# create an instance of FinancialLineItem from a dict
financial_line_item_form_dict = financial_line_item.from_dict(financial_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


