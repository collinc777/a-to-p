# Word

Word of a document      Attributes:         text (str): Text detected in the word         bounding_boxes (Sequence[BoundingBox]): Bounding boxes of the words in the word         confidence (float): Confidence score of the word     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text detected in the word | 
**bounding_box** | [**BoundingBox**](BoundingBox.md) | Bounding boxes of the words in the word | 
**confidence** | **int** | Confidence score of the word | 

## Example

```python
from openapi_client.models.word import Word

# TODO update the JSON string below
json = "{}"
# create an instance of Word from a JSON string
word_instance = Word.from_json(json)
# print the JSON string representation of the object
print(Word.to_json())

# convert the object into a dict
word_dict = word_instance.to_dict()
# create an instance of Word from a dict
word_form_dict = word.from_dict(word_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


