from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category_type import CategoryType
from ..models.date_and_time_sub_category_type import DateAndTimeSubCategoryType
from ..models.financial_information_sub_category_type import FinancialInformationSubCategoryType
from ..models.identification_numbers_sub_category_type import IdentificationNumbersSubCategoryType
from ..models.location_information_sub_category_type import LocationInformationSubCategoryType
from ..models.miscellaneous_sub_category_type import MiscellaneousSubCategoryType
from ..models.organization_sub_category_type import OrganizationSubCategoryType
from ..models.other_sub_category_type import OtherSubCategoryType
from ..models.personal_information_sub_category_type import PersonalInformationSubCategoryType

T = TypeVar("T", bound="AnonymizationEntity")


@_attrs_define
class AnonymizationEntity:
    """This model represents an entity extracted from the text.

    Attributes:
        offset (int): The offset of the entity in the text.
        length (int): The lenght of the entity in the text.
        category (CategoryType): The category of the entity.
        subcategory (SubCategoryType): The subcategory of the entity.
        original_label (str): The original label of the entity.
        content (str): The content of the entity.


    Attributes:
        offset (int):
        length (int):
        category (CategoryType): This enum are used to categorize the explicit content extracted from the text
        subcategory (Union[DateAndTimeSubCategoryType, FinancialInformationSubCategoryType,
            IdentificationNumbersSubCategoryType, LocationInformationSubCategoryType, MiscellaneousSubCategoryType,
            OrganizationSubCategoryType, OtherSubCategoryType, PersonalInformationSubCategoryType]):
        original_label (str):
        content (str):
        confidence_score (int):
    """

    offset: int
    length: int
    category: CategoryType
    subcategory: Union[
        DateAndTimeSubCategoryType,
        FinancialInformationSubCategoryType,
        IdentificationNumbersSubCategoryType,
        LocationInformationSubCategoryType,
        MiscellaneousSubCategoryType,
        OrganizationSubCategoryType,
        OtherSubCategoryType,
        PersonalInformationSubCategoryType,
    ]
    original_label: str
    content: str
    confidence_score: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        offset = self.offset

        length = self.length

        category = self.category.value

        subcategory: str
        if isinstance(self.subcategory, FinancialInformationSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, PersonalInformationSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, IdentificationNumbersSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, MiscellaneousSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, OrganizationSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, DateAndTimeSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, LocationInformationSubCategoryType):
            subcategory = self.subcategory.value
        else:
            subcategory = self.subcategory.value

        original_label = self.original_label

        content = self.content

        confidence_score = self.confidence_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offset": offset,
                "length": length,
                "category": category,
                "subcategory": subcategory,
                "original_label": original_label,
                "content": content,
                "confidence_score": confidence_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        offset = d.pop("offset")

        length = d.pop("length")

        category = CategoryType(d.pop("category"))

        def _parse_subcategory(
            data: object,
        ) -> Union[
            DateAndTimeSubCategoryType,
            FinancialInformationSubCategoryType,
            IdentificationNumbersSubCategoryType,
            LocationInformationSubCategoryType,
            MiscellaneousSubCategoryType,
            OrganizationSubCategoryType,
            OtherSubCategoryType,
            PersonalInformationSubCategoryType,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_0 = FinancialInformationSubCategoryType(data)

                return subcategory_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_1 = PersonalInformationSubCategoryType(data)

                return subcategory_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_2 = IdentificationNumbersSubCategoryType(data)

                return subcategory_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_3 = MiscellaneousSubCategoryType(data)

                return subcategory_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_4 = OrganizationSubCategoryType(data)

                return subcategory_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_5 = DateAndTimeSubCategoryType(data)

                return subcategory_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_6 = LocationInformationSubCategoryType(data)

                return subcategory_type_6
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            subcategory_type_7 = OtherSubCategoryType(data)

            return subcategory_type_7

        subcategory = _parse_subcategory(d.pop("subcategory"))

        original_label = d.pop("original_label")

        content = d.pop("content")

        confidence_score = d.pop("confidence_score")

        anonymization_entity = cls(
            offset=offset,
            length=length,
            category=category,
            subcategory=subcategory,
            original_label=original_label,
            content=content,
            confidence_score=confidence_score,
        )

        anonymization_entity.additional_properties = d
        return anonymization_entity

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
