from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.category_type import CategoryType
from ..models.content_sub_category_type import ContentSubCategoryType
from ..models.drug_and_alcohol_sub_category_type import DrugAndAlcoholSubCategoryType
from ..models.finance_sub_category_type import FinanceSubCategoryType
from ..models.hate_and_extremism_sub_category_type import HateAndExtremismSubCategoryType
from ..models.other_sub_category_type import OtherSubCategoryType
from ..models.safe_sub_category_type import SafeSubCategoryType
from ..models.sexual_sub_category_type import SexualSubCategoryType
from ..models.toxic_sub_category_type import ToxicSubCategoryType
from ..models.violence_sub_category_type import ViolenceSubCategoryType

T = TypeVar("T", bound="ExplicitItem")


@_attrs_define
class ExplicitItem:
    """
    Attributes:
        label (str):
        likelihood (int):
        likelihood_score (int):
        category (CategoryType): This enum are used to categorize the explicit content extracted from the text
        subcategory (Union[ContentSubCategoryType, DrugAndAlcoholSubCategoryType, FinanceSubCategoryType,
            HateAndExtremismSubCategoryType, OtherSubCategoryType, SafeSubCategoryType, SexualSubCategoryType,
            ToxicSubCategoryType, ViolenceSubCategoryType]):
    """

    label: str
    likelihood: int
    likelihood_score: int
    category: CategoryType
    subcategory: Union[
        ContentSubCategoryType,
        DrugAndAlcoholSubCategoryType,
        FinanceSubCategoryType,
        HateAndExtremismSubCategoryType,
        OtherSubCategoryType,
        SafeSubCategoryType,
        SexualSubCategoryType,
        ToxicSubCategoryType,
        ViolenceSubCategoryType,
    ]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        likelihood = self.likelihood

        likelihood_score = self.likelihood_score

        category = self.category.value

        subcategory: str
        if isinstance(self.subcategory, ToxicSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, ContentSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, SexualSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, ViolenceSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, DrugAndAlcoholSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, FinanceSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, HateAndExtremismSubCategoryType):
            subcategory = self.subcategory.value
        elif isinstance(self.subcategory, SafeSubCategoryType):
            subcategory = self.subcategory.value
        else:
            subcategory = self.subcategory.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "likelihood": likelihood,
                "likelihood_score": likelihood_score,
                "category": category,
                "subcategory": subcategory,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        likelihood = d.pop("likelihood")

        likelihood_score = d.pop("likelihood_score")

        category = CategoryType(d.pop("category"))

        def _parse_subcategory(
            data: object,
        ) -> Union[
            ContentSubCategoryType,
            DrugAndAlcoholSubCategoryType,
            FinanceSubCategoryType,
            HateAndExtremismSubCategoryType,
            OtherSubCategoryType,
            SafeSubCategoryType,
            SexualSubCategoryType,
            ToxicSubCategoryType,
            ViolenceSubCategoryType,
        ]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_0 = ToxicSubCategoryType(data)

                return subcategory_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_1 = ContentSubCategoryType(data)

                return subcategory_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_2 = SexualSubCategoryType(data)

                return subcategory_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_3 = ViolenceSubCategoryType(data)

                return subcategory_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_4 = DrugAndAlcoholSubCategoryType(data)

                return subcategory_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_5 = FinanceSubCategoryType(data)

                return subcategory_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_6 = HateAndExtremismSubCategoryType(data)

                return subcategory_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                subcategory_type_7 = SafeSubCategoryType(data)

                return subcategory_type_7
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            subcategory_type_8 = OtherSubCategoryType(data)

            return subcategory_type_8

        subcategory = _parse_subcategory(d.pop("subcategory"))

        explicit_item = cls(
            label=label,
            likelihood=likelihood,
            likelihood_score=likelihood_score,
            category=category,
            subcategory=subcategory,
        )

        explicit_item.additional_properties = d
        return explicit_item

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
