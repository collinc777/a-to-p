# FinancialPaymentInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_due** | **int** | Amount due for payment. | [optional] 
**amount_tip** | **int** | Tip amount in a financial transaction. | [optional] 
**amount_shipping** | **int** | Shipping cost in a financial transaction. | [optional] 
**amount_change** | **int** | Change amount in a financial transaction. | [optional] 
**amount_paid** | **int** | Amount already paid in a financial transaction. | [optional] 
**total** | **int** | Total amount in the invoice. | [optional] 
**subtotal** | **int** | Subtotal amount in a financial transaction. | [optional] 
**total_tax** | **int** | Total tax amount in a financial transaction. | [optional] 
**tax_rate** | **int** | Tax rate applied in a financial transaction. | [optional] 
**discount** | **int** | Discount amount applied in a financial transaction. | [optional] 
**gratuity** | **int** | Gratuity amount in a financial transaction. | [optional] 
**service_charge** | **int** | Service charge in a financial transaction. | [optional] 
**previous_unpaid_balance** | **int** | Previous unpaid balance in a financial transaction. | [optional] 
**prior_balance** | **int** | Prior balance before the current financial transaction. | [optional] 
**payment_terms** | **str** | Terms and conditions for payment. | [optional] 
**payment_method** | **str** | Payment method used in the financial transaction. | [optional] 
**payment_card_number** | **str** | Card number used in the payment. | [optional] 
**payment_auth_code** | **str** | Authorization code for the payment. | [optional] 
**shipping_handling_charge** | **int** | Charge for shipping and handling in a financial transaction. | [optional] 
**transaction_number** | **str** | Unique identifier for the financial transaction. | [optional] 
**transaction_reference** | **str** | Reference number for the financial transaction. | [optional] 

## Example

```python
from openapi_client.models.financial_payment_information import FinancialPaymentInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialPaymentInformation from a JSON string
financial_payment_information_instance = FinancialPaymentInformation.from_json(json)
# print the JSON string representation of the object
print(FinancialPaymentInformation.to_json())

# convert the object into a dict
financial_payment_information_dict = financial_payment_information_instance.to_dict()
# create an instance of FinancialPaymentInformation from a dict
financial_payment_information_form_dict = financial_payment_information.from_dict(financial_payment_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


