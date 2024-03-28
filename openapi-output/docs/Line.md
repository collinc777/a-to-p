# Line

Line of a document      Attributes:         text (str): Text detected in the line         bounding_boxes (Sequence[BoundingBox]): Bounding boxes of the words in the line         words (Sequence[Word]): List of words of the line         confidence (float): Confidence of the line     

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Text detected in the line | 
**words** | [**List[Word]**](Word.md) | List of words | [optional] 
**bounding_box** | [**BoundingBox**](BoundingBox.md) | Bounding boxes of the words in the line | 
**confidence** | **int** | Confidence of the line | 

## Example

```python
from openapi_client.models.line import Line

# TODO update the JSON string below
json = "{}"
# create an instance of Line from a JSON string
line_instance = Line.from_json(json)
# print the JSON string representation of the object
print(Line.to_json())

# convert the object into a dict
line_dict = line_instance.to_dict()
# create an instance of Line from a dict
line_form_dict = line.from_dict(line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


